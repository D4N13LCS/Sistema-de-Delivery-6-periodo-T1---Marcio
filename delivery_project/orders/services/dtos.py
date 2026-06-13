from dataclasses import dataclass

@dataclass(frozen=True)
class DeliveryData:
    tipo: str
    taxa: float
    pagamento: str