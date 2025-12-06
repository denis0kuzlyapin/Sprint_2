class EmployeeSalary:

    hourly_payment = 400

    @classmethod
    def get_hours(cls, name, hours, rest_days, email):
        if hours is None:
            hours = (7 - rest_days) * 8
        return cls(name, hours, rest_days, email)

    @classmethod
    def get_email(cls, name, hours, rest_days, email):
        if email is None:
            email = f"{name}@email.com"
        return cls(name, hours, rest_days, email)

    @classmethod
    def set_hourly_payment(cls, new_hourly_payment):
        cls.hourly_payment = new_hourly_payment

    @staticmethod
    def salary(hours, new_hourly_payment):
        return hours * new_hourly_payment

    def __init__(self, name, hours, rest_days, email):
        self.name = name
        self.hours = hours
        self.rest_days = rest_days
        self.email = email

    def employee_information(self):
        print(f"Имя: {self.name}"
              f"\nВремя работы: {self.hours}"
              f"\nКол-во выходных: {self.rest_days}"
              f"\nПочта: {self.email}")


EmployeeSalary.set_hourly_payment(350)  # Изменяем часовую ставку
# Создаем первого работника, вызвав метод класса get_email(cls) т.к. неизвестен email
employee_1 = EmployeeSalary.get_email('Денис', 45, 2, None)
employee_1.employee_information()  # Выводим информацию о первом работнике
# Создаем второго работника, вызвав метод класса get_hours(cls) т.к. неизвестно кол-во часов
employee_2 = EmployeeSalary.get_hours('Майк', None, 1, 'Wazovski@email.com')
employee_2.employee_information()  # Выводим информацию о втором работнике

# Вызываем метод класса salary(cls), передав в качестве аргументов часы первого работника и переменную с текущей часовой ставкой
pay_1 = EmployeeSalary.salary(employee_1.hours, EmployeeSalary.hourly_payment)
# Вызываем метод класса salary(cls), передав в качестве аргументов часы второго работника и переменную с текущей часовой ставкой
pay_2 = EmployeeSalary.salary(employee_2.hours, EmployeeSalary.hourly_payment)
print(pay_1)  # Выводим сумму для певрого работника
print(pay_2)  # Выводим сумму для второго работника
