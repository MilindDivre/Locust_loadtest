from locust import User,task

class FirstTest(User):

    @task
    def launch(self):
        print("Launching the url")

    @task
    def search(self):
        print("searching the application")