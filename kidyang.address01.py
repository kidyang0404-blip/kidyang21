class address:
    def __init__(
        self,
        name: str,
        phone: str,
        email: str,
        address: str,
        group: str = "friend, family"
    ):
        self.name = name 
        self.phone = phone 
        self.email = email 
        self.address = address
        self.group = group 

    def print_info(self): 
        print(f"이름: {self.name}") 
        print(f"전화: {self.phone}") 
        print(f"이메일: {self.email}")
        print(f"주소: {self.address}") 
        print(f"그룹: {self.group}")
        print("-" * 16)

    def to_dict(self) -> dict:
        return {
            "name": self.name, 
            "phone": self.phone, 
            "email": self.email, 
            "address": self.address, 
            "group": self.group, 
            } 
    @classmethod 
    def from_dict(cls, data: dict):
        return cls(
            name = data["name"],
            phone = data["phone"], 
            email = data['email'], 
            address = data["address"], 
            group = data["group"], 
        )   