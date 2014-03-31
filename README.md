### Setup

# Install Dependencies
- virtualenv venv
- source venv/bin/activate
- pip install -r requirements.txt

# Start Message Broker
- sudo rabbitmq server

# Start worker
- cd receiver/app
- celery -A tasks worker --loglevel=info

# Start server
- cd sender
- python server.py

# Test it!
Navigate your browser to localhost:5001. When you submit the form, the *sender* submits the mult task to the worker, which processes it and returns the result. 