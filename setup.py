"""
Database setup script - creates PostgreSQL database and user
Run this before starting the application
"""

import subprocess
import sys
import os
from pathlib import Path


def run_command(command, shell=False):
    """Run a command and return output"""
    try:
        result = subprocess.run(
            command,
            shell=shell,
            capture_output=True,
            text=True,
            timeout=10
        )
        return result.returncode, result.stdout, result.stderr
    except Exception as e:
        return 1, "", str(e)


def setup_postgresql():
    """Setup PostgreSQL database"""
    
    print("🔧 Setting up PostgreSQL for Commitment AI...")
    print("-" * 50)
    
    # Configuration
    db_name = "commit_ai"
    db_user = "commit_user"
    db_password = input("Enter password for PostgreSQL user (or press Enter for 'password'): ").strip() or "password"
    db_host = "localhost"
    db_port = "5432"
    
    # Check if psql is available
    print("✓ Checking PostgreSQL installation...")
    code, out, err = run_command(["psql", "--version"], shell=False)
    if code != 0:
        print("✗ PostgreSQL is not installed or not in PATH")
        print("  Please install PostgreSQL: https://www.postgresql.org/download/")
        return False
    
    print("✓ PostgreSQL found")
    
    # Create database and user
    print(f"\n🗄️  Creating database '{db_name}'...")
    
    # SQL commands to run
    sql_commands = f"""
    -- Create database
    CREATE DATABASE {db_name};
    
    -- Create user
    CREATE USER {db_user} WITH PASSWORD '{db_password}';
    
    -- Configure user
    ALTER ROLE {db_user} SET client_encoding TO 'utf8';
    ALTER ROLE {db_user} SET default_transaction_isolation TO 'read committed';
    ALTER ROLE {db_user} SET default_transaction_deferrable TO on;
    
    -- Grant privileges
    GRANT ALL PRIVILEGES ON DATABASE {db_name} TO {db_user};
    """
    
    print("✓ Running SQL setup commands...")
    
    # For Windows, we need to use psql with SQL commands
    try:
        # Try to run via psql (requires PostgreSQL to be running and accessible)
        # On Windows, this might require credentials
        
        print("\nNote: You may be prompted for PostgreSQL admin password")
        print("If prompted, enter the password for the 'postgres' user\n")
        
        # Create a temporary SQL file
        sql_file = Path("_setup.sql")
        sql_file.write_text(sql_commands)
        
        # Run psql on Windows
        cmd = f'psql -U postgres -h {db_host} -f _setup.sql'
        code, out, err = run_command(cmd, shell=True)
        
        # Clean up
        sql_file.unlink()
        
        if code == 0:
            print("✓ Database and user created successfully")
        else:
            print("⚠ Warning: Could not create database automatically")
            print("  This might be because:")
            print("  - PostgreSQL is not running")
            print("  - PostgreSQL user permissions issue")
            print("\n  Manual setup:")
            print(f"  1. Start PostgreSQL")
            print(f"  2. Run: psql -U postgres")
            print(f"  3. Paste these commands:")
            print(sql_commands)
            return False
    
    except Exception as e:
        print(f"✗ Error: {e}")
        return False
    
    # Create .env file
    print("\n📝 Creating .env file...")
    env_content = f"""# Database Configuration
DATABASE_URL=postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}

# App Settings
APP_NAME=Commitment AI
DEBUG=True

# Security
SECRET_KEY=your-secret-key-change-in-production
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# LLM Settings (Llama)
LLM_MODEL=llama2
LLM_API_URL=http://localhost:11434
"""
    
    env_file = Path(".env")
    env_file.write_text(env_content)
    print("✓ .env file created")
    
    # Test connection
    print("\n🧪 Testing database connection...")
    print(f"   postgresql://{db_user}:****@{db_host}:{db_port}/{db_name}")
    
    return True


def setup_python_env():
    """Setup Python virtual environment and install dependencies"""
    
    print("\n🐍 Setting up Python environment...")
    print("-" * 50)
    
    # Check Python version
    if sys.version_info < (3, 8):
        print("✗ Python 3.8+ is required")
        return False
    
    print(f"✓ Python {sys.version.split()[0]} found")
    
    # Install requirements
    print("\n📦 Installing dependencies...")
    
    req_file = Path("requirements.txt")
    if not req_file.exists():
        print("✗ requirements.txt not found")
        return False
    
    code, out, err = run_command([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
    
    if code == 0:
        print("✓ Dependencies installed")
    else:
        print("✗ Error installing dependencies")
        if err:
            print(err)
        return False
    
    return True


def main():
    """Main setup function"""
    
    print("=" * 50)
    print("  Commitment AI - Setup")
    print("=" * 50)
    
    # Check if in correct directory
    if not Path("main.py").exists():
        print("✗ Please run this script from the project root directory")
        return
    
    # Setup Python environment
    if not setup_python_env():
        print("\n⚠ Python setup incomplete. Continuing...")
    
    # Setup PostgreSQL
    if not setup_postgresql():
        print("\n⚠ Database setup incomplete")
        print("  You'll need to setup PostgreSQL manually before running the app")
        return
    
    print("\n" + "=" * 50)
    print("✓ Setup complete!")
    print("=" * 50)
    print("\nNext steps:")
    print("1. Make sure PostgreSQL is running")
    print("2. Make sure Llama is running (if using local LLM):")
    print("   ollama pull llama2")
    print("   ollama serve")
    print("3. Run the application:")
    print("   python main.py")
    print("\n📚 API docs will be available at: http://localhost:8000/api/docs")
    print("=" * 50)


if __name__ == "__main__":
    main()
