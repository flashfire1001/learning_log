from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


def register(request):
    """Register a new user."""
    if request.method != 'POST':
        # Display blank registration form.
        form = UserCreationForm()
    else:
        # Process completed form.
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # Log the user in and then redirect to home page.
            login(request, new_user)
            return redirect('learning_logs:index')

    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'registration/register.html', context)



'''you learned how forms allow users to add new topics and entries, and edit existing entries. You then learned how to implement user accounts. You gave existing users the ability to log in and out, and used Django’s default UserCreationForm to let people create new accounts.
User Accounts 431
After building a simple user authentication and registration system, you
restricted access to logged-in users for certain pages using the @login_required
decorator. You then assigned data to specific users through a foreign key
relationship. You also learned to migrate the database when the migration
requires you to specify some default data.
Finally, you learned how to make sure a user can only see data that
belongs to them by modifying the view functions. You retrieved appropriate
data using the filter() method, and compared the owner of the
requested data to the currently logged-in user.
Here is my question :
how can I delete a topic
how can I public a blog/entries(probably send it to the administrator; and let the info of the admin to be non-opacity)

'''