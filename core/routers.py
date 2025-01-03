class OrdersRouter:
    """
    A router to control all database operations on the `Order` model to `orders.db`.
    """

    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'orders':
            return 'orders'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'orders':
            return 'orders'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == 'orders' or obj2._meta.app_label == 'orders':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'orders':
            return db == 'orders'
        return None
