class Mediator:
    def send_message(self, msg, department):
        pass


class Department:
    def __init__(self, mediator=None):
        self.mediator = mediator

    def send_message(self, msg):
        self.mediator.send_message(msg, self)

    def receive_message(self, msg):
        pass

class HRDepartment(Department):
    def receive_message(self, msg):
        print(f"HR Department received msg: {msg}")

class FinanceDepartment(Department):
    def receive_message(self, msg):
        print(f"Finance department received msg: {msg}")

class OfficeMediator(Mediator):
    def __init__(self):
        self.hr = None
        self.finance = None

    def set_hr(self, hr):
        self.hr = hr

    def set_finance(self, finance):
        self.finance = finance

    def send_message(self, msg, department):
        if department == self.hr:
            if self.finance:
                self.finance.receive_message(msg)

        elif department == self.finance:
            if self.hr:
                self.hr.receive_message(msg)


# Test the implementation
mediator = OfficeMediator()
hr = HRDepartment(mediator)
finance = FinanceDepartment(mediator)

mediator.set_hr(hr)
mediator.set_finance(finance)

hr.send_message("HR Updates for all departments")


# Finance department received msg: HR Updates for all departments