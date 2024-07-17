class LuxuryWatch:
    watches_created = 0

    def __init__(self):
        LuxuryWatch.watches_created += 1

    @staticmethod
    def validate_engraving_text(text):
        if len(text) > 40:
            raise ValueError("Engraving text cannot be longer than 40 characters.")
        if not text.isalnum():
            raise ValueError("Engraving text must be alphanumerical with no spaces.")
        return True
        
        
    @classmethod
    def get_number_of_watches_created(cls):
        return cls.watches_created
        
        
        
# Test cases
try:
    # Create a watch with no engraving
    watch1 = LuxuryWatch()
    print("Watch 1 created. Total watches:", LuxuryWatch.get_number_of_watches_created())

    # Create a watch with a correct text for engraving
    watch2 = LuxuryWatch.validate_engraving_text("LuxuryWatch2024")
    print("Watch 2 created with engraving. Total watches:", LuxuryWatch.get_number_of_watches_created())

    # Try to create a watch with incorrect text
    watch3 = LuxuryWatch.validate_engraving_text("foo@baz.com")
    
    # Create a watch with a correct text for engraving
    watch4 = LuxuryWatch.validate_engraving_text("LuxuryWatch2024")
    print("Watch 4 created with engraving. Total watches:", LuxuryWatch.get_number_of_watches_created())

except ValueError as e:
    print("Failed to create watch with engraving:", e)

print("Final number of watches created:", LuxuryWatch.get_number_of_watches_created())


