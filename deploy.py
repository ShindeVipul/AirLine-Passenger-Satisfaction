from flask import Flask, render_template, request
import pickle


app = Flask(__name__)
# load the model
model = pickle.load(open('savedmodel.pkl', 'rb'))

@app.route('/')
def home():
    result = ''
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    gender= request.form['gender']
    Age_Group = request.form['Age_Group']
    customer_type = request.form['customer_type']
    Type_of_Travel = request.form['Type_of_Travel']
    Class = request.form['Class']
    Flight_Distance = request.form['Flight_Distance']
    Inflight_wifi_service = request.form['Inflight_wifi_service']
    DepartureArrival_time_convenient= request.form['DepartureArrival_time_convenient']
    Ease_of_Online_booking= request.form['Ease_of_Online_booking']
    Gate_location= request.form['Gate_location']
    Food_and_drink= request.form['Food_and_drink']
    Online_boarding= request.form['Online_boarding']
    Seat_comfort= request.form['Seat_comfort']
    Inflight_entertainment= request.form['Inflight_entertainment']
    On_board_service= request.form['On_board_service']
    Leg_room_service= request.form['Leg_room_service']
    Baggage_handling= request.form['Baggage_handling']
    Checkin_service= request.form['Checkin_service']
    Inflight_service= request.form['Inflight_service']
    Cleanliness= request.form['Cleanliness']
    Departure_Delay_in_Minutes= request.form['Departure_Delay_in_Minutes']
    Arrival_Delay_in_Minutes= request.form['Arrival_Delay_in_Minutes']
    result = model.predict([[gender,Age_Group,customer_type,Type_of_Travel,Class,Flight_Distance,Inflight_wifi_service,
    DepartureArrival_time_convenient,Ease_of_Online_booking,Gate_location,Food_and_drink,Online_boarding,Seat_comfort,Inflight_entertainment,
    On_board_service,Leg_room_service,Baggage_handling,Checkin_service,Inflight_service,Cleanliness,Departure_Delay_in_Minutes,Arrival_Delay_in_Minutes]])[0]
    
    return render_template('predict.html', data=result)



if __name__ == '__main__':
    app.run(debug=True)
