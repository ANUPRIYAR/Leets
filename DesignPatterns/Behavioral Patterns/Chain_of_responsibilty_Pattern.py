from enum import Enum, auto

class QueryType(Enum):
    TECHNICAL = auto()
    BILLING = auto()
    GENERAL = auto()

class SupportHandler():
    def __init__(self):
        self.next_handler = None

    def set_next_handler(self, handler):
        self.next_handler = handler

    def handle_request(self, query_type, message):
        pass


class TechnicalSupportHandler(SupportHandler):
    def handle_request(self, query_type, message):
        if query_type == QueryType.TECHNICAL:
            print(f"Technical Support : Handling Query: {message}")
        elif self.next_handler is not None:
            self.next_handler.handle_request(query_type, message)

class BillingSupportHandler(SupportHandler):
    def handle_request(self, query_type, message):
        if query_type == QueryType.BILLING:
            print(f"Billing support: Handling Query - {message}")
        elif self.next_handler is not None:
            self.next_handler.handle_request(query_type, message)


class GeneralSupportHandler(SupportHandler):
    def handle_request(self, query_type, message):
        if query_type == QueryType.GENERAL:
            print(f"General support: Handling Query - {message}")
        elif self.next_handler is not None:
            self.next_handler.handle_request(query_type, message)


# Client
technical_support = TechnicalSupportHandler()
billing_support = BillingSupportHandler()
general_support = GeneralSupportHandler()


