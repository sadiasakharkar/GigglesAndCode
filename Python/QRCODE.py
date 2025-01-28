import qrcode

def generate_qr(event_id):
    # Create URL for the event attendance tracking
    url = f"https://example.com/attendance?event_id={event_id}"
    
    # Generate QR code
    qr = qrcode.make(url)
    
    # Save the QR code as an image
    qr.save(f"event_{event_id}_qr.png")
    
# Example usage
generate_qr("12345")
