class Crop:
    def __init__(self, name: str, crop_type: str, growth_conditions: dict):
        self.name = name
        self.crop_type = crop_type
        self.growth_conditions = growth_conditions

    def __repr__(self):
        return f"<Crop(name={self.name}, type={self.crop_type})>"

    def is_suitable_for_conditions(self, conditions: dict) -> bool:
        for key, value in self.growth_conditions.items():
            if key in conditions and conditions[key] < value:
                return False
        return True

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            name=data.get("name"),
            crop_type=data.get("crop_type"),
            growth_conditions=data.get("growth_conditions", {})
        )