from models import Activity, TimeUnit

def some_pereare():
    print 'some_pereare'

def compute_scores():
    try:
        timeunit = TimeUnit.objects.get(name='django unittest')
        some_pereare()
    except TimeUnit.DoesNotExist:
        try:
            activity, is_new = Activity.objects.get_or_create(name='django coding')
            if is_new:
                print 'activity created'
            else:
                print 'activity found'
        except Activity.MultipleObjectsReturned:
            print 'activity lol no'
        timeunit = TimeUnit(activity=activity, name='django unittest')


if __name__ == "__main__":
	compute_scores()