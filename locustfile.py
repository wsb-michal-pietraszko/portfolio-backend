import random
from locust import HttpUser, task, between

class MyDjangoUser(HttpUser):
    wait_time = between(1, 5)

    @task(3)
    def index(self):
        self.client.get("/")

    @task(1)
    def hello(self):
        response = self.client.get("/hello")
        csrftoken = response.cookies['csrftoken']
        self.client.post(
            "/hello",
            {
                "csrfmiddlewaretoken": csrftoken,
                "name": f"User{random.randint(1, 100)}"
            },
            headers={"Referer": self.client.base_url + "/hello"},
            cookies={"csrftoken": csrftoken},
        )
