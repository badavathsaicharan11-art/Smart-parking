from flask import Flask, render_template, request
app = Flask(__name__)
occupied = set()
vehicle_slots = {}
parking = {
    "A1":["A2","A3"], "A2":["A4","A3"], "A3":["A4"],
    "A4":["B1"], "B1":["B2"], "B2":["B3"],
    "B3":["B4"], "B4":["C1"], "C1":["C2"],
    "C2":["C3"], "C3":["C4"], "C4":[]
}
def heuristic(slot):
    distance = {
        "A1": 1, "A2": 2, "A3": 1, "A4": 2,
        "B1": 3, "B2": 4, "B3": 5, "B4": 6,
        "C1": 7, "C2": 8, "C3": 9, "C4": 10
    }
    return distance[slot]
def bfs():
    queue = ["A1"]
    visited = set()
    while queue:
        slot = queue.pop(0)
        if slot in visited:
            continue
        visited.add(slot)
        if slot not in occupied:
            return slot
        queue += sorted(parking[slot], key=heuristic)
    return None
@app.route("/")
def home():
    return render_template("index.html", occupied=occupied)
@app.route("/allocate", methods=["POST"])
def allocate():
    vehicle = request.form.get("vehicle")

    if vehicle in vehicle_slots:
        slot = vehicle_slots[vehicle]
    else:
        slot = bfs()
    if slot:
        vehicle_slots[vehicle] = slot
        occupied.add(slot)
        result = f"Vehicle {vehicle} is allocated to parking slot {slot}."
    else:
        result = "No parking slot available."
    return render_template("index.html", result=result, occupied=occupied)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=False)