class HourlyEmployee:
    """Employee Paid by the hour + commission"""

    pay_rate: float = 0
    hours_worked: int = 0
    pay_per_commission: float = 100
    commission_count: int = 0

    def __init__(
        self,
        pay_rate: float = 0,
        hours_worked: int = 0,
        pay_per_commission: float = 100,
        commission_count: int = 0,
    ):
        self.pay_rate = pay_rate
        self.hours_worked = hours_worked
        self.pay_per_commission = pay_per_commission
        self.commission_count = commission_count

    def compute_pay(self) -> float:
        """Return payrate * hours worked + commission_count * pay_per_commission"""
        return (self.pay_rate * self.hours_worked) + (
            self.commission_count * self.pay_per_commission
        )


class SalaryEmployee:
    """Employee Paid monthly + commission"""

    monthly_salary: float = 0
    months_worked: int = 0
    pay_per_commission: float = 100
    commission_count: int = 0

    def __init__(
        self,
        monthly_salary: float = 0,
        months_worked: int = 0,
        pay_per_commission: float = 100,
        commission_count: int = 0,
    ):
        self.monthly_salary = monthly_salary
        self.months_worked = months_worked
        self.pay_per_commission = pay_per_commission
        self.commission_count = commission_count

    def compute_pay(self) -> float:
        """Return monthly_salary * months worked + commission_count * pay_per_commission"""

        return (self.monthly_salary * self.months_worked) + (
            self.commission_count * self.pay_per_commission
        )


class Freelancer:
    """Paid by purely from commission"""

    commission_rate: float = 0
    commission_count: int = 0

    def __init__(self, commission_rate: float = 0, commission_count: int = 0) -> None:
        self.commission_count = commission_count
        self.commission_rate = commission_rate

    def compute_pay(self) -> float:
        return self.commission_rate * self.commission_count


def main() -> None:
    hr_employee = HourlyEmployee(
        pay_rate=100, hours_worked=9, pay_per_commission=100, commission_count=1
    )

    # EXPECTED: 1000
    print(hr_employee.compute_pay())

    sal_employee = SalaryEmployee(
        monthly_salary=900, months_worked=1, pay_per_commission=100, commission_count=1
    )
    # EXPECTED: 1000
    print(sal_employee.compute_pay())

    fr_employee = Freelancer(commission_rate=1000, commission_count=1)
    # EXPECTED: 100
    print(fr_employee.compute_pay())


if __name__ == "__main__":
    main()
