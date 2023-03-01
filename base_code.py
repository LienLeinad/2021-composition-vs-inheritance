import abc
from typing import Optional


class PaymentCalculator(abc.ABC):
    """Represents how the employee is paid"""

    @abc.abstractmethod
    def get_payment(self) -> float:
        """gets how much the employee is paid"""
        pass


class CommissionCalculator(abc.ABC):
    """Represents the commission payment of the employee"""

    @abc.abstractmethod
    def get_payment(self) -> float:
        """gets how much commission is added to the pay"""
        pass


class SalaryPaymentCalculator(PaymentCalculator):
    def __init__(self, monthly_salary: float, months_worked: int):
        self.monthly_salary = monthly_salary
        self.months_worked = months_worked

    def get_payment(self) -> float:
        return self.monthly_salary * self.months_worked


class HourlyPaymentCalculator(PaymentCalculator):
    def __init__(self, hourly_salary: float, hours_worked: int):
        self.hourly_salary = hourly_salary
        self.hours_worked = hours_worked

    def get_payment(self) -> float:
        return self.hourly_salary * self.hours_worked


class NoPaymentCalculator(PaymentCalculator):
    def get_payment(self) -> float:
        return 0


class BaseCommissionCalculator(CommissionCalculator):
    def __init__(self, pay_per_commission: float, commission_count: int):
        self.pay_per_commission = pay_per_commission
        self.commission_count = commission_count

    def get_payment(self) -> float:
        return self.pay_per_commission * self.commission_count


class BaseWithBonusCommissionCalculator(BaseCommissionCalculator):
    def __init__(self, pay_per_commission: float, commission_count: int, bonus: float):
        self.pay_per_commission = pay_per_commission
        self.commission_count = commission_count
        self.bonus = bonus

    def get_payment(self) -> float:
        return super().get_payment() + self.bonus


class Employee:
    payment_calculator: PaymentCalculator
    commission_calculator: Optional[CommissionCalculator] = None

    def __init__(
        self,
        payment_calculator: PaymentCalculator,
        commission_calculator: Optional[CommissionCalculator],
    ):
        self.payment_calculator = payment_calculator
        self.commission_calculator = commission_calculator

    def compute_pay(self) -> float:
        base_pay = self.payment_calculator.get_payment()
        if self.commission_calculator is not None:
            base_pay += self.commission_calculator.get_payment()
        return base_pay


def main() -> None:
    hr_employee_no_commission = Employee(
        payment_calculator=HourlyPaymentCalculator(hourly_salary=100, hours_worked=10),
        commission_calculator=None,
    )

    # EXPECTED: 1000
    print(hr_employee_no_commission.compute_pay())

    hr_employee_w_commission = Employee(
        HourlyPaymentCalculator(hourly_salary=100, hours_worked=9),
        commission_calculator=BaseCommissionCalculator(
            pay_per_commission=100, commission_count=1
        ),
    )
    # EXPECTED: 1000
    print(hr_employee_w_commission.compute_pay())

    sal_employee_no_commission = Employee(
        payment_calculator=SalaryPaymentCalculator(
            monthly_salary=1000, months_worked=1
        ),
        commission_calculator=None,
    )
    # EXPECTED: 1000
    print(sal_employee_no_commission.compute_pay())

    sal_employee_w_commission = Employee(
        payment_calculator=SalaryPaymentCalculator(monthly_salary=900, months_worked=1),
        commission_calculator=BaseCommissionCalculator(100, 1),
    )
    # EXPECTED: 1000
    print(sal_employee_w_commission.compute_pay())

    fr_employee_no_bonus = Employee(
        payment_calculator=NoPaymentCalculator(),
        commission_calculator=BaseCommissionCalculator(
            pay_per_commission=1000, commission_count=1
        ),
    )
    # EXPECTED: 100
    print(fr_employee_no_bonus.compute_pay())

    fr_employee_w_bonus = Employee(
        payment_calculator=NoPaymentCalculator(),
        commission_calculator=BaseWithBonusCommissionCalculator(
            pay_per_commission=900, commission_count=1, bonus=100
        ),
    )

    # EXPECTED: 1000
    print(fr_employee_w_bonus.compute_pay())


if __name__ == "__main__":
    main()
