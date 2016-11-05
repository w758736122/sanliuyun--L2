from django.shortcuts import render

def editor(request):

    context = {}

    editor_page = render(request, 'editoring.html', context)
    return editor_page

def login(request):
    context = {}
    # if request.method == 'GET':
    #     form = AuthenticationForm
    # if request.method == 'POST':
    #     form = AuthenticationForm(data=request.POST)
    #     if form.is_valid():
    #         login(request, form.get_user())
    #         return redirect(to='desktop')
    #
    # context['form'] = form
    return render(request, 'login.html', context)
