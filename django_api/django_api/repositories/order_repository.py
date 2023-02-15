from django_api.models.t_order import TOrder


class OrderRepository():

    def register(self, data):
        data = TOrder(commands=data["commands"])
        data.save()

        return data
