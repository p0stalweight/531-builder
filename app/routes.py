from flask import render_template, flash, redirect, request, url_for
from app import app
from app.forms import WorkoutForm
from app.weightbreakdown import WeightBreakdown

@app.route('/', methods=['GET', 'POST'])
def index():
    form = WorkoutForm()
    if form.validate_on_submit():
        press = request.form.get('press_max')
        deadlift = request.form.get('deadlift_max')
        bench = request.form.get('bench_max')
        squat = request.form.get('squat_max')

        wb = WeightBreakdown(press, deadlift, bench, squat)
        workout = wb.build_workout()   
        return render_template('workout.html', workout=workout)
    return render_template('index.html', form=form)
