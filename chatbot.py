import re

def issue_resolution_chatbot(user_input):
    # Convert user input to lowercase for case-insensitivity
    user_input = user_input.lower()

    # Define patterns for common user queries about the specific issue
    patterns = {
        'login_issue': r'\b(?:login|sign in)\b',
        'password_reset': r'\b(?:forgot password|reset password)\b',
        'account_creation': r'\b(?:create account|sign up)\b',
        'payment_problem': r'\b(?:payment issue|transaction problem)\b',
        'technical_error': r'\b(?:technical error|site not working)\b',
        'order_tracking': r'\b(?:track order|order status)\b',
        'product_issue': r'\b(?:product problem|defective item)\b',
        'contact_support': r'\b(?:contact support|customer service)\b',
        'general_inquiry': r'\b(?:help|information)\b'
    }

    # Check user input against defined patterns
    for key, pattern in patterns.items():
        if re.search(pattern, user_input):
            return get_response(key)

    # Check for greeting, exit, or gratitude
    if re.search(r'\b(?:hello)\b', user_input):
        return "Hello! How can I assist you with the issue?"

    elif re.search(r'\b(?:bye|thank you)\b', user_input):
        return "Goodbye! If you have more questions, feel free to ask."

    # If no specific rule matches
    return "I'm sorry, I didn't understand that. How can I assist you with the issue?"

def get_response(key):
    # Define responses for each identified issue
    responses = {
        'login_issue': "If you are facing login issues, please make sure you are using the correct credentials. If the problem persists, you can reset your password.",
        'password_reset': "To reset your password, click on the 'Forgot Password' link on the login page and follow the instructions provided.",
        'account_creation': "To create an account, click on the 'Sign Up' or 'Create Account' option on the website's homepage.",
        'payment_problem': "If you are experiencing payment issues, double-check your payment details and ensure they are entered correctly. If the problem continues, contact our support team.",
        'technical_error': "If you are encountering technical errors or the site is not working, please try clearing your browser cache and cookies. If the issue persists, contact our technical support.",
        'order_tracking': "To track your order or check its status, go to the 'Order Tracking' section on the website and enter your order details.",
        'product_issue': "If you have received a defective item, please contact our customer service with details about the issue and your order number.",
        'contact_support': "If you need further assistance, please contact our customer support team through the 'Contact Us' page or the provided customer service number.",
        'general_inquiry': "For general inquiries or more information, feel free to ask. I'm here to help!"
    }

    return responses.get(key, "I'm sorry, there seems to be an issue. Please contact our customer support for assistance.")

# Example usage
print("Chatbot: Hello! How can I assist you today?")
while True:
    user_input = input("You: ")
    if re.search(r'\b(?:bye|thank you)\b', user_input.lower()):
        print("Chatbot: Goodbye! If you have more questions, feel free to ask.")
        break
    response = issue_resolution_chatbot(user_input)
    print("Chatbot:", response)
