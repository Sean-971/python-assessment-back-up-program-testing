import logging

# Configure logging to append to 'app.log'
logging.basicConfig(
    filename='backup.log', 
    filemode='a', # 'a' means append (this is the default)
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
chosen_error = ""
# Write log messages
def SetErrorMessage():

    Error_Code_list =["File not found in config list","File in config but file does not exist", "Program does not want to work for some reason"]
    chosen_error = random.choice((Error_Code_list))

def main():
    SetErrorMessage

    logging.info("This message is appended to the log file.")
    logging.error(f'An error occurred during execution. Error: {chosen_error}')

if __name__ == "__main__":
    main()