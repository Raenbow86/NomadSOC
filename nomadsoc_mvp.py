# NomadSOC MVP v0.1
# A simple public Wi-Fi risk checker for travelers, van lifers, remote workers, and everyday users.

def ask_yes_no(question):
    while True:
        answer = input(question + " (yes/no): ").strip().lower()

        if answer in ["yes", "y"]:
            return True
        elif answer in ["no", "n"]:
            return False
        else:
            print("Please answer yes or no.")


print("Welcome to NomadSOC")
print("Let's check your public Wi-Fi risk.\n")

risk_score = 0
risk_reasons = []
recommendations = []

public_wifi = ask_yes_no("Are you using public or shared Wi-Fi?")
if public_wifi:
    risk_score += 2
    recommendations.append("Be careful on public/shared Wi-Fi.")

password_protected = ask_yes_no("Is the Wi-Fi password-protected?")
if not password_protected:
    risk_score += 2
    recommendations.append("Open Wi-Fi is riskier because anyone nearby may be able to connect.")

official_network = ask_yes_no("Are you sure this is the official network for the location?")
if not official_network:
    risk_score += 2
    recommendations.append("Double-check the network name with the business or location staff.")

using_vpn = ask_yes_no("Are you using a VPN?")
if not using_vpn:
    risk_score += 2
    recommendations.append("Use a VPN before logging into sensitive accounts.")

sensitive_activity = ask_yes_no("Are you doing sensitive activity like banking, healthcare, school, legal, or work logins?")
if sensitive_activity:
    risk_score += 3
    recommendations.append("Avoid sensitive activity unless your connection is protected.")

device_updated = ask_yes_no("Is your device updated?")
if not device_updated:
    risk_score += 1
    recommendations.append("Update your device when possible to reduce security risk.")

firewall_on = ask_yes_no("Is your firewall turned on?")
if not firewall_on:
    risk_score += 1
    recommendations.append("Turn on your firewall for extra protection.")


print("\n--- NomadSOC Result ---")
print(f"Risk Score: {risk_score}")

if risk_score <= 2:
    result = "Low Risk"
    message = "Basic browsing should be okay. Still avoid unnecessary sensitive activity."
elif risk_score <= 5:
    result = "Moderate Risk"
    message = "Use caution. A VPN is recommended, especially for logins."
elif risk_score <= 8:
    result = "VPN Recommended"
    message = "This connection has several risk factors. Use a VPN before continuing."
else:
    result = "High Risk"
    message = "Avoid banking, healthcare, legal, school, or work logins on this connection."

print(f"Result: {result}")
print(f"Recommendation: {message}")

print("\nSafety Notes:")
for recommendation in recommendations:
    print(f"- {recommendation}")

print("\nThank you for using NomadSOC.")
