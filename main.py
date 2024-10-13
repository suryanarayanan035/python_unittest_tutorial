import argparse
import sys
sys.path.append("./")
from user_service import UserService 
parser = argparse.ArgumentParser()

parser.add_argument('file_type') # positional argument
parser.add_argument('file_name') # positional argument
args = parser.parse_args()
try:
    UserService.save_users_to_file(args.file_name, args.file_type)
except Exception as e:
    print(f"Some Error Occured.")
    print(f"Error: {e}")
else:
    print(f"User data is saved to the file {args.file_name}")
