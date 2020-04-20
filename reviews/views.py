from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Review
from .forms import ReviewForm


def get_reviews(request):
    """
    Create a view that will return a list
    of reviews that were published prior to 'now'
    and render them
    """
    reviews = Review.objects.filter(created_date__lte=timezone.now()
        ).order_by('-created_date')
    return render(request, "reviews.html", {'reviews': reviews})


def review_detail(request, pk):
    """
    Create a view that returns a single
    review and
    render it to the 'reviewdetail.html' template.
    Or return a 404 error if the review is
    not found
    """
    review = get_object_or_404(Review, pk=pk)
    review.save()
    return render(request, "reviewdetail.html", {'review': review})


def create_or_edit_review(request, pk=None):

    review = get_object_or_404(Review, pk=pk) if pk else None
    if request.method == "POST":
        form = ReviewForm(request.POST, request.FILES, instance=review)
        if form.is_valid():
            review = form.save()
            return redirect(review_detail, review.pk)
    else:
        form = ReviewForm(instance=review)
    return render(request, 'reviewform.html', {'form': form})