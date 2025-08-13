from django.core.mail import EmailMultiAlternatives
from django.utils.html import strip_tags

def send_welcome_email(user):
    subject = "Welcome to Our Site!"
    from_email = "no-reply@example.com"  # Change this to your sender address
    to = [user.email]

    html_content = f"""
    <html>
        <body style="font-family: Arial, sans-serif; color: #333;">
            <h2>Welcome, {user.username}!</h2>
            <p>Thanks for signing up! We're excited to have you on board.</p>
            <p>Here are a few things you can do next:</p>
            <ul>
                <li>Explore our latest content</li>
                <li>Update your profile</li>
                <li>Invite your friends</li>
            </ul>
            <p>Happy exploring!</p>
            <p style="color: gray; font-size: 12px;">&copy; 2025 Our Site</p>
        </body>
    </html>
    """

    text_content = strip_tags(html_content)  # Fallback text

    msg = EmailMultiAlternatives(subject, text_content, from_email, to)
    msg.attach_alternative(html_content, "text/html")
    msg.send()
