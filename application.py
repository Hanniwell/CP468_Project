from src.webapp import application
if __name__ == '__main__':
    # application.run(debug=False, host = '0.0.0.0') #when running on ec2
    application.run(debug=False)