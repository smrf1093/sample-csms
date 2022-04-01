round_precision = 3


class ChargingPriceComponent(object):
    def calculate_price(self, **kwargs) -> float:
        raise NotImplementedError()


class EnergyCalculatorComponent(ChargingPriceComponent):
    def __init__(self, energy, meter_start, meter_stop) -> None:
        super().__init__()
        self.energy = energy
        self.meter_start = meter_start
        self.meter_stop = meter_stop

    def calculate_price(
        self,
    ) -> float:
        kwh_usage = (self.meter_stop - self.meter_start) / 1000
        return round(self.energy * kwh_usage, round_precision)


class TimeCalculatorComponent(ChargingPriceComponent):
    def __init__(self, time, time_start, time_stop) -> None:
        super().__init__()
        self.time = time
        self.time_start = time_start
        self.time_stop = time_stop

    def calculate_price(self) -> float:
        time_diff = (self.time_stop - self.time_start).seconds / 3600
        return round(self.time * time_diff, round_precision)


class TransactionCalculatorComponent(ChargingPriceComponent):
    def __init__(self, transaction) -> None:
        super().__init__()
        self.transaction = transaction

    def calculate_price(self) -> float:
        return round(self.transaction, round_precision)


class ChargingPriceCalculator(object):
    def __init__(self, components: dict):
        self.components = components

    def calculate_price(self, **kwargs) -> dict:
        components_prices = dict()
        for name, component in self.components.items():
            components_prices[name] = component.calculate_price(**kwargs)
        return components_prices
