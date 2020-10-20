from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, RadioField, SubmitField
from wtforms.validators import DataRequired

class WorkoutForm(FlaskForm):
    press_max = IntegerField('Military Press', validators=[DataRequired()])
    deadlift_max = IntegerField('Deadlift', validators=[DataRequired()])
    bench_max = IntegerField('Bench Press', validators=[DataRequired()])
    squat_max = IntegerField('Squat', validators=[DataRequired()])
    submit = SubmitField('Generate Workout')