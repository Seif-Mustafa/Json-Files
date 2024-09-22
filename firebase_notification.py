import requests
import firebase_admin
from firebase_admin import credentials, messaging

def get_notifications_to_be_sent():
 
    url = "http://65.109.83.174:8005/servytestapi/resources/Notifications/getNotificationsToBePushed"

    try:
        response = requests.get(url)
        
        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()  # Parse the JSON response
            # print(data)  # Print or process the data as needed
            return data['allNotificationsToBePushed']
        else:
            print(f"Failed to Update data: {response.status_code}")

    except Exception as e:
        print(f"An error occurred: {e}")


def update_notifications_to_be_pushed():
    url = "http://65.109.83.174:8005/servytestapi/resources/Notifications/updateNotificationsToBePushed"

    try:
        response = requests.post(url)
        
        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()  # Parse the JSON response
            # print(data)  # Print or process the data as needed
            print("Updated")
        else:
            print(f"Failed to retrieve data: {response.status_code}")

    except Exception as e:
        print(f"An error occurred: {e}")



def send_fcm_notification(token, title, body):
    message = messaging.Message(
        notification=messaging.Notification(
            title=title,
            body=body,
        ),
        token=token,
    )
    
    response = messaging.send(message)
    print('Successfully sent message:', response)



# Example usage
if __name__ == "__main__":

    notifications = get_notifications_to_be_sent()

    # print(notifications)

    if len(notifications)>0:
    # Initialize the Admin SDK
        cred = credentials.Certificate("/home/oracle/servyReports/FirebaseNotification/servy-app-firebase-adminsdk-a60pv-9684717665.json")
        firebase_admin.initialize_app(cred)
        for notification in notifications:
            if len(notification["mobileFCM"])>0:
                send_fcm_notification(notification["mobileFCM"], "Servy", notification["body"])
            # print(notification["mobileFCM"])
            # print(notification["title"])
            # print(notification["body"])
            # print("#########################")
        update_notifications_to_be_pushed()
    





