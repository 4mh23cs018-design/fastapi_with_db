import sys
import os

print(f"CWD: {os.getcwd()}")
try:
    from routes.user_routes import router
    print("SUCCESS: Imported routes.user_routes")
except Exception as e:
    print(f"ERROR importing routes.user_routes: {e}")
    sys.exit(1)

try:
    from main import app
    print("SUCCESS: Imported main")
except Exception as e:
    print(f"ERROR importing main: {e}")
    sys.exit(1)

try:
    from repositories.user_repo import User_Repo
    print("SUCCESS: Imported repositories.user_repo.User_Repo")
except Exception as e:
    print(f"ERROR importing User_Repo: {e}")
    sys.exit(1)
