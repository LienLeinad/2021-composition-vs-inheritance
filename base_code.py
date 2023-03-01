import abc


class Employee(abc.ABC):
    @abc.abstractmethod
    def compute_pay(self) -> float:
        pass


class HourlyEmployee(Employee):
    """Employee Paid by the hour + commission"""

    pay_rate: float = 0
    hours_worked: int = 0

    def __init__(
        self,
        pay_rate: float = 0,
        hours_worked: int = 0,
    ):
        self.pay_rate = pay_rate
        self.hours_worked = hours_worked

    def compute_pay(self) -> float:
        """Return payrate * hours worked + commission_count * pay_per_commission"""
        return self.pay_rate * self.hours_worked


class HourlyCommissionedEmployee(HourlyEmployee):
    pay_per_commission: float = 10
    commission_count: int = 0

    def __init__(
        self,
        pay_rate: float = 0,
        hours_worked: int = 0,
        pay_per_commission: float = 10,
        commission_count: int = 0,
    ):
        self.pay_rate = pay_rate
        self.hours_worked = hours_worked
        self.pay_per_commission = pay_per_commission
        self.commission_count = commission_count

    def compute_pay(self) -> float:
        return super().compute_pay() + (self.commission_count * self.pay_per_commission)


class SalaryEmployee(Employee):
    """Employee Paid monthly"""

    monthly_salary: float = 0
    months_worked: int = 0

    def __init__(
        self,
        monthly_salary: float = 0,
        months_worked: int = 0,
    ):
        self.monthly_salary = monthly_salary
        self.months_worked = months_worked

    def compute_pay(self) -> float:
        """Return monthly_salary * months worked + commission_count * pay_per_commission"""
        return self.monthly_salary * self.months_worked


class SalaryCommissionedEmployee(SalaryEmployee):
    pay_per_commission: float = 10
    commission_count: int = 0

    def __init__(
        self,
        monthly_salary: float = 0,
        months_worked: int = 0,
        pay_per_commission: float = 10,
        commission_count: int = 0,
    ):
        self.monthly_salary = monthly_salary
        self.months_worked = months_worked
        self.pay_per_commission = pay_per_commission
        self.commission_count = commission_count

    def compute_pay(self) -> float:
        return super().compute_pay() + +(
            self.commission_count * self.pay_per_commission
        )


class Freelancer(Employee):
    """Paid by purely from commission"""

    commission_rate: float = 0
    commission_count: int = 0

    def __init__(self, commission_rate: float = 0, commission_count: int = 0) -> None:
        self.commission_count = commission_count
        self.commission_rate = commission_rate

    def compute_pay(self) -> float:
        return self.commission_rate * self.commission_count


class FreeLancerWithBonus(Freelancer):
    bonus: float = 0

    def __init__(
        self, commission_rate: float = 0, commission_count: int = 0, bonus: float = 0
    ) -> None:
        self.commission_count = commission_count
        self.commission_rate = commission_rate
        self.bonus = bonus

    def compute_pay(self) -> float:
        return super().compute_pay() + self.bonus


def main() -> None:
    hr_employee_no_commission = HourlyEmployee(pay_rate=100, hours_worked=10)

    # EXPECTED: 1000
    print(hr_employee_no_commission.compute_pay())

    hr_employee_w_commission = HourlyCommissionedEmployee(
        pay_rate=100, hours_worked=9, pay_per_commission=100, commission_count=1
    )
    # EXPECTED: 1000
    print(hr_employee_w_commission.compute_pay())

    sal_employee_no_commission = SalaryEmployee(monthly_salary=1000, months_worked=1)
    # EXPECTED: 1000
    print(sal_employee_no_commission.compute_pay())

    sal_employee_w_commission = SalaryCommissionedEmployee(
        monthly_salary=900, months_worked=1, commission_count=1, pay_per_commission=100
    )
    # EXPECTED: 1000
    print(sal_employee_w_commission.compute_pay())

    fr_employee_no_bonus = Freelancer(commission_rate=1000, commission_count=1)
    # EXPECTED: 100
    print(fr_employee_no_bonus.compute_pay())

    fr_employee_w_bonus = FreeLancerWithBonus(
        commission_rate=900, commission_count=1, bonus=100
    )

    # EXPECTED: 1000
    print(fr_employee_w_bonus.compute_pay())


if __name__ == "__main__":
    main()
