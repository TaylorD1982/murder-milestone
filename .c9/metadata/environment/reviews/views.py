{"filter":false,"title":"views.py","tooltip":"/reviews/views.py","undoManager":{"mark":77,"position":77,"stack":[[{"start":{"row":0,"column":0},"end":{"row":3,"column":0},"action":"remove","lines":["from django.shortcuts import render","","# Create your views here.",""],"id":2},{"start":{"row":0,"column":0},"end":{"row":45,"column":63},"action":"insert","lines":["from django.shortcuts import render, get_object_or_404, redirect","from django.utils import timezone","from .models import Post","from .forms import BlogPostForm","","","def get_posts(request):","    \"\"\"","    Create a view that will return a list","    of Posts that were published prior to 'now'","    and render them to the 'blogposts.html' template","    \"\"\"","    posts = Post.objects.filter(published_date__lte=timezone.now()","        ).order_by('-published_date')","    return render(request, \"blogposts.html\", {'posts': posts})","","","def post_detail(request, pk):","    \"\"\"","    Create a view that returns a single","    Post object based on the post ID (pk) and","    render it to the 'postdetail.html' template.","    Or return a 404 error if the post is","    not found","    \"\"\"","    post = get_object_or_404(Post, pk=pk)","    post.views += 1","    post.save()","    return render(request, \"postdetail.html\", {'post': post})","","","def create_or_edit_post(request, pk=None):","    \"\"\"","    Create a view that allows us to create","    or edit a post depending if the Post ID","    is null or not","    \"\"\"","    post = get_object_or_404(Post, pk=pk) if pk else None","    if request.method == \"POST\":","        form = BlogPostForm(request.POST, request.FILES, instance=post)","        if form.is_valid():","            post = form.save()","            return redirect(post_detail, post.pk)","    else:","        form = BlogPostForm(instance=post)","    return render(request, 'blogpostform.html', {'form': form})"]}],[{"start":{"row":2,"column":23},"end":{"row":2,"column":24},"action":"remove","lines":["t"],"id":3},{"start":{"row":2,"column":22},"end":{"row":2,"column":23},"action":"remove","lines":["s"]},{"start":{"row":2,"column":21},"end":{"row":2,"column":22},"action":"remove","lines":["o"]},{"start":{"row":2,"column":20},"end":{"row":2,"column":21},"action":"remove","lines":["P"]}],[{"start":{"row":2,"column":20},"end":{"row":2,"column":21},"action":"insert","lines":["R"],"id":4},{"start":{"row":2,"column":21},"end":{"row":2,"column":22},"action":"insert","lines":["e"]},{"start":{"row":2,"column":22},"end":{"row":2,"column":23},"action":"insert","lines":["v"]},{"start":{"row":2,"column":23},"end":{"row":2,"column":24},"action":"insert","lines":["i"]},{"start":{"row":2,"column":24},"end":{"row":2,"column":25},"action":"insert","lines":["e"]},{"start":{"row":2,"column":25},"end":{"row":2,"column":26},"action":"insert","lines":["w"]}],[{"start":{"row":3,"column":26},"end":{"row":3,"column":27},"action":"remove","lines":["t"],"id":5},{"start":{"row":3,"column":25},"end":{"row":3,"column":26},"action":"remove","lines":["s"]},{"start":{"row":3,"column":24},"end":{"row":3,"column":25},"action":"remove","lines":["o"]},{"start":{"row":3,"column":23},"end":{"row":3,"column":24},"action":"remove","lines":["P"]},{"start":{"row":3,"column":22},"end":{"row":3,"column":23},"action":"remove","lines":["g"]},{"start":{"row":3,"column":21},"end":{"row":3,"column":22},"action":"remove","lines":["o"]},{"start":{"row":3,"column":20},"end":{"row":3,"column":21},"action":"remove","lines":["l"]},{"start":{"row":3,"column":19},"end":{"row":3,"column":20},"action":"remove","lines":["B"]}],[{"start":{"row":3,"column":19},"end":{"row":3,"column":20},"action":"insert","lines":["R"],"id":6},{"start":{"row":3,"column":20},"end":{"row":3,"column":21},"action":"insert","lines":["e"]},{"start":{"row":3,"column":21},"end":{"row":3,"column":22},"action":"insert","lines":["v"]},{"start":{"row":3,"column":22},"end":{"row":3,"column":23},"action":"insert","lines":["i"]},{"start":{"row":3,"column":23},"end":{"row":3,"column":24},"action":"insert","lines":["e"]},{"start":{"row":3,"column":24},"end":{"row":3,"column":25},"action":"insert","lines":["w"]}],[{"start":{"row":6,"column":4},"end":{"row":6,"column":13},"action":"remove","lines":["get_posts"],"id":7},{"start":{"row":6,"column":4},"end":{"row":6,"column":15},"action":"insert","lines":["get_reviews"]}],[{"start":{"row":17,"column":4},"end":{"row":17,"column":15},"action":"remove","lines":["post_detail"],"id":8},{"start":{"row":17,"column":4},"end":{"row":17,"column":17},"action":"insert","lines":["review_detail"]},{"start":{"row":42,"column":28},"end":{"row":42,"column":39},"action":"remove","lines":["post_detail"]},{"start":{"row":42,"column":28},"end":{"row":42,"column":41},"action":"insert","lines":["review_detail"]}],[{"start":{"row":31,"column":4},"end":{"row":31,"column":23},"action":"remove","lines":["create_or_edit_post"],"id":9},{"start":{"row":31,"column":4},"end":{"row":31,"column":25},"action":"insert","lines":["create_or_edit_review"]}],[{"start":{"row":14,"column":51},"end":{"row":14,"column":52},"action":"remove","lines":["s"],"id":10},{"start":{"row":14,"column":50},"end":{"row":14,"column":51},"action":"remove","lines":["t"]},{"start":{"row":14,"column":49},"end":{"row":14,"column":50},"action":"remove","lines":["s"]},{"start":{"row":14,"column":48},"end":{"row":14,"column":49},"action":"remove","lines":["o"]},{"start":{"row":14,"column":47},"end":{"row":14,"column":48},"action":"remove","lines":["p"]}],[{"start":{"row":14,"column":47},"end":{"row":14,"column":48},"action":"insert","lines":["r"],"id":11},{"start":{"row":14,"column":48},"end":{"row":14,"column":49},"action":"insert","lines":["e"]},{"start":{"row":14,"column":49},"end":{"row":14,"column":50},"action":"insert","lines":["v"]},{"start":{"row":14,"column":50},"end":{"row":14,"column":51},"action":"insert","lines":["i"]},{"start":{"row":14,"column":51},"end":{"row":14,"column":52},"action":"insert","lines":["e"]},{"start":{"row":14,"column":52},"end":{"row":14,"column":53},"action":"insert","lines":["w"]},{"start":{"row":14,"column":53},"end":{"row":14,"column":54},"action":"insert","lines":["s"]}],[{"start":{"row":14,"column":61},"end":{"row":14,"column":62},"action":"remove","lines":["s"],"id":12},{"start":{"row":14,"column":60},"end":{"row":14,"column":61},"action":"remove","lines":["t"]},{"start":{"row":14,"column":59},"end":{"row":14,"column":60},"action":"remove","lines":["s"]},{"start":{"row":14,"column":58},"end":{"row":14,"column":59},"action":"remove","lines":["o"]},{"start":{"row":14,"column":57},"end":{"row":14,"column":58},"action":"remove","lines":["p"]}],[{"start":{"row":14,"column":57},"end":{"row":14,"column":58},"action":"insert","lines":["r"],"id":13},{"start":{"row":14,"column":58},"end":{"row":14,"column":59},"action":"insert","lines":["e"]},{"start":{"row":14,"column":59},"end":{"row":14,"column":60},"action":"insert","lines":["v"]},{"start":{"row":14,"column":60},"end":{"row":14,"column":61},"action":"insert","lines":["i"]},{"start":{"row":14,"column":61},"end":{"row":14,"column":62},"action":"insert","lines":["e"]},{"start":{"row":14,"column":62},"end":{"row":14,"column":63},"action":"insert","lines":["w"]},{"start":{"row":14,"column":63},"end":{"row":14,"column":64},"action":"insert","lines":["s"]}],[{"start":{"row":12,"column":7},"end":{"row":12,"column":8},"action":"remove","lines":["t"],"id":14},{"start":{"row":12,"column":6},"end":{"row":12,"column":7},"action":"remove","lines":["s"]},{"start":{"row":12,"column":5},"end":{"row":12,"column":6},"action":"remove","lines":["o"]},{"start":{"row":12,"column":4},"end":{"row":12,"column":5},"action":"remove","lines":["p"]}],[{"start":{"row":12,"column":4},"end":{"row":12,"column":5},"action":"insert","lines":["r"],"id":15},{"start":{"row":12,"column":5},"end":{"row":12,"column":6},"action":"insert","lines":["e"]},{"start":{"row":12,"column":6},"end":{"row":12,"column":7},"action":"insert","lines":["v"]},{"start":{"row":12,"column":7},"end":{"row":12,"column":8},"action":"insert","lines":["i"]},{"start":{"row":12,"column":8},"end":{"row":12,"column":9},"action":"insert","lines":["e"]},{"start":{"row":12,"column":9},"end":{"row":12,"column":10},"action":"insert","lines":["w"]},{"start":{"row":12,"column":10},"end":{"row":12,"column":11},"action":"insert","lines":["s"]}],[{"start":{"row":12,"column":10},"end":{"row":12,"column":11},"action":"remove","lines":["s"],"id":16}],[{"start":{"row":12,"column":17},"end":{"row":12,"column":18},"action":"remove","lines":["t"],"id":17},{"start":{"row":12,"column":16},"end":{"row":12,"column":17},"action":"remove","lines":["s"]},{"start":{"row":12,"column":15},"end":{"row":12,"column":16},"action":"remove","lines":["o"]},{"start":{"row":12,"column":14},"end":{"row":12,"column":15},"action":"remove","lines":["P"]}],[{"start":{"row":12,"column":14},"end":{"row":12,"column":15},"action":"insert","lines":["R"],"id":18},{"start":{"row":12,"column":15},"end":{"row":12,"column":16},"action":"insert","lines":["e"]},{"start":{"row":12,"column":16},"end":{"row":12,"column":17},"action":"insert","lines":["v"]},{"start":{"row":12,"column":17},"end":{"row":12,"column":18},"action":"insert","lines":["i"]},{"start":{"row":12,"column":18},"end":{"row":12,"column":19},"action":"insert","lines":["e"]},{"start":{"row":12,"column":19},"end":{"row":12,"column":20},"action":"insert","lines":["w"]}],[{"start":{"row":25,"column":7},"end":{"row":25,"column":8},"action":"remove","lines":["t"],"id":19},{"start":{"row":25,"column":6},"end":{"row":25,"column":7},"action":"remove","lines":["s"]},{"start":{"row":25,"column":5},"end":{"row":25,"column":6},"action":"remove","lines":["o"]},{"start":{"row":25,"column":4},"end":{"row":25,"column":5},"action":"remove","lines":["p"]}],[{"start":{"row":25,"column":4},"end":{"row":25,"column":5},"action":"insert","lines":["r"],"id":20},{"start":{"row":25,"column":5},"end":{"row":25,"column":6},"action":"insert","lines":["e"]},{"start":{"row":25,"column":6},"end":{"row":25,"column":7},"action":"insert","lines":["v"]},{"start":{"row":25,"column":7},"end":{"row":25,"column":8},"action":"insert","lines":["i"]},{"start":{"row":25,"column":8},"end":{"row":25,"column":9},"action":"insert","lines":["e"]},{"start":{"row":25,"column":9},"end":{"row":25,"column":10},"action":"insert","lines":["w"]}],[{"start":{"row":25,"column":34},"end":{"row":25,"column":35},"action":"remove","lines":["t"],"id":21},{"start":{"row":25,"column":33},"end":{"row":25,"column":34},"action":"remove","lines":["s"]},{"start":{"row":25,"column":32},"end":{"row":25,"column":33},"action":"remove","lines":["o"]},{"start":{"row":25,"column":31},"end":{"row":25,"column":32},"action":"remove","lines":["P"]}],[{"start":{"row":25,"column":31},"end":{"row":25,"column":32},"action":"insert","lines":["R"],"id":22},{"start":{"row":25,"column":32},"end":{"row":25,"column":33},"action":"insert","lines":["e"]},{"start":{"row":25,"column":33},"end":{"row":25,"column":34},"action":"insert","lines":["v"]},{"start":{"row":25,"column":34},"end":{"row":25,"column":35},"action":"insert","lines":["i"]},{"start":{"row":25,"column":35},"end":{"row":25,"column":36},"action":"insert","lines":["e"]},{"start":{"row":25,"column":36},"end":{"row":25,"column":37},"action":"insert","lines":["w"]}],[{"start":{"row":26,"column":7},"end":{"row":26,"column":8},"action":"remove","lines":["t"],"id":23},{"start":{"row":26,"column":6},"end":{"row":26,"column":7},"action":"remove","lines":["s"]},{"start":{"row":26,"column":5},"end":{"row":26,"column":6},"action":"remove","lines":["o"]},{"start":{"row":26,"column":4},"end":{"row":26,"column":5},"action":"remove","lines":["p"]}],[{"start":{"row":26,"column":4},"end":{"row":26,"column":5},"action":"insert","lines":["r"],"id":24},{"start":{"row":26,"column":5},"end":{"row":26,"column":6},"action":"insert","lines":["e"]},{"start":{"row":26,"column":6},"end":{"row":26,"column":7},"action":"insert","lines":["v"]},{"start":{"row":26,"column":7},"end":{"row":26,"column":8},"action":"insert","lines":["i"]},{"start":{"row":26,"column":8},"end":{"row":26,"column":9},"action":"insert","lines":["e"]},{"start":{"row":26,"column":9},"end":{"row":26,"column":10},"action":"insert","lines":["w"]}],[{"start":{"row":27,"column":7},"end":{"row":27,"column":8},"action":"remove","lines":["t"],"id":25},{"start":{"row":27,"column":6},"end":{"row":27,"column":7},"action":"remove","lines":["s"]},{"start":{"row":27,"column":5},"end":{"row":27,"column":6},"action":"remove","lines":["o"]},{"start":{"row":27,"column":4},"end":{"row":27,"column":5},"action":"remove","lines":["p"]}],[{"start":{"row":27,"column":4},"end":{"row":27,"column":5},"action":"insert","lines":["r"],"id":26},{"start":{"row":27,"column":5},"end":{"row":27,"column":6},"action":"insert","lines":["e"]},{"start":{"row":27,"column":6},"end":{"row":27,"column":7},"action":"insert","lines":["v"]},{"start":{"row":27,"column":7},"end":{"row":27,"column":8},"action":"insert","lines":["i"]},{"start":{"row":27,"column":8},"end":{"row":27,"column":9},"action":"insert","lines":["e"]},{"start":{"row":27,"column":9},"end":{"row":27,"column":10},"action":"insert","lines":["w"]}],[{"start":{"row":28,"column":31},"end":{"row":28,"column":32},"action":"remove","lines":["t"],"id":27},{"start":{"row":28,"column":30},"end":{"row":28,"column":31},"action":"remove","lines":["s"]},{"start":{"row":28,"column":29},"end":{"row":28,"column":30},"action":"remove","lines":["o"]},{"start":{"row":28,"column":28},"end":{"row":28,"column":29},"action":"remove","lines":["p"]}],[{"start":{"row":28,"column":28},"end":{"row":28,"column":29},"action":"insert","lines":["r"],"id":28},{"start":{"row":28,"column":29},"end":{"row":28,"column":30},"action":"insert","lines":["e"]},{"start":{"row":28,"column":30},"end":{"row":28,"column":31},"action":"insert","lines":["v"]},{"start":{"row":28,"column":31},"end":{"row":28,"column":32},"action":"insert","lines":["i"]},{"start":{"row":28,"column":32},"end":{"row":28,"column":33},"action":"insert","lines":["e"]},{"start":{"row":28,"column":33},"end":{"row":28,"column":34},"action":"insert","lines":["w"]}],[{"start":{"row":28,"column":53},"end":{"row":28,"column":54},"action":"remove","lines":["t"],"id":29},{"start":{"row":28,"column":52},"end":{"row":28,"column":53},"action":"remove","lines":["s"]},{"start":{"row":28,"column":51},"end":{"row":28,"column":52},"action":"remove","lines":["o"]},{"start":{"row":28,"column":50},"end":{"row":28,"column":51},"action":"remove","lines":["p"]}],[{"start":{"row":28,"column":50},"end":{"row":28,"column":51},"action":"insert","lines":["r"],"id":30},{"start":{"row":28,"column":51},"end":{"row":28,"column":52},"action":"insert","lines":["e"]},{"start":{"row":28,"column":52},"end":{"row":28,"column":53},"action":"insert","lines":["v"]},{"start":{"row":28,"column":53},"end":{"row":28,"column":54},"action":"insert","lines":["i"]},{"start":{"row":28,"column":54},"end":{"row":28,"column":55},"action":"insert","lines":["e"]},{"start":{"row":28,"column":55},"end":{"row":28,"column":56},"action":"insert","lines":["w"]}],[{"start":{"row":28,"column":62},"end":{"row":28,"column":63},"action":"remove","lines":["t"],"id":31},{"start":{"row":28,"column":61},"end":{"row":28,"column":62},"action":"remove","lines":["s"]},{"start":{"row":28,"column":60},"end":{"row":28,"column":61},"action":"remove","lines":["o"]},{"start":{"row":28,"column":59},"end":{"row":28,"column":60},"action":"remove","lines":["p"]}],[{"start":{"row":28,"column":59},"end":{"row":28,"column":60},"action":"insert","lines":["r"],"id":32},{"start":{"row":28,"column":60},"end":{"row":28,"column":61},"action":"insert","lines":["e"]},{"start":{"row":28,"column":61},"end":{"row":28,"column":62},"action":"insert","lines":["v"]},{"start":{"row":28,"column":62},"end":{"row":28,"column":63},"action":"insert","lines":["i"]},{"start":{"row":28,"column":63},"end":{"row":28,"column":64},"action":"insert","lines":["e"]},{"start":{"row":28,"column":64},"end":{"row":28,"column":65},"action":"insert","lines":["w"]}],[{"start":{"row":37,"column":7},"end":{"row":37,"column":8},"action":"remove","lines":["t"],"id":33},{"start":{"row":37,"column":6},"end":{"row":37,"column":7},"action":"remove","lines":["s"]},{"start":{"row":37,"column":5},"end":{"row":37,"column":6},"action":"remove","lines":["o"]},{"start":{"row":37,"column":4},"end":{"row":37,"column":5},"action":"remove","lines":["p"]}],[{"start":{"row":37,"column":4},"end":{"row":37,"column":5},"action":"insert","lines":["r"],"id":34},{"start":{"row":37,"column":5},"end":{"row":37,"column":6},"action":"insert","lines":["e"]},{"start":{"row":37,"column":6},"end":{"row":37,"column":7},"action":"insert","lines":["v"]},{"start":{"row":37,"column":7},"end":{"row":37,"column":8},"action":"insert","lines":["i"]},{"start":{"row":37,"column":8},"end":{"row":37,"column":9},"action":"insert","lines":["e"]},{"start":{"row":37,"column":9},"end":{"row":37,"column":10},"action":"insert","lines":["w"]}],[{"start":{"row":37,"column":34},"end":{"row":37,"column":35},"action":"remove","lines":["t"],"id":35},{"start":{"row":37,"column":33},"end":{"row":37,"column":34},"action":"remove","lines":["s"]},{"start":{"row":37,"column":32},"end":{"row":37,"column":33},"action":"remove","lines":["o"]},{"start":{"row":37,"column":31},"end":{"row":37,"column":32},"action":"remove","lines":["P"]}],[{"start":{"row":37,"column":31},"end":{"row":37,"column":32},"action":"insert","lines":["R"],"id":36},{"start":{"row":37,"column":32},"end":{"row":37,"column":33},"action":"insert","lines":["e"]},{"start":{"row":37,"column":33},"end":{"row":37,"column":34},"action":"insert","lines":["v"]},{"start":{"row":37,"column":34},"end":{"row":37,"column":35},"action":"insert","lines":["i"]},{"start":{"row":37,"column":35},"end":{"row":37,"column":36},"action":"insert","lines":["e"]},{"start":{"row":37,"column":36},"end":{"row":37,"column":37},"action":"insert","lines":["w"]}],[{"start":{"row":38,"column":29},"end":{"row":38,"column":30},"action":"remove","lines":["T"],"id":37},{"start":{"row":38,"column":28},"end":{"row":38,"column":29},"action":"remove","lines":["S"]},{"start":{"row":38,"column":27},"end":{"row":38,"column":28},"action":"remove","lines":["O"]},{"start":{"row":38,"column":26},"end":{"row":38,"column":27},"action":"remove","lines":["P"]}],[{"start":{"row":38,"column":26},"end":{"row":38,"column":27},"action":"insert","lines":["R"],"id":38},{"start":{"row":38,"column":27},"end":{"row":38,"column":28},"action":"insert","lines":["e"]},{"start":{"row":38,"column":28},"end":{"row":38,"column":29},"action":"insert","lines":["v"]},{"start":{"row":38,"column":29},"end":{"row":38,"column":30},"action":"insert","lines":["i"]},{"start":{"row":38,"column":30},"end":{"row":38,"column":31},"action":"insert","lines":["e"]},{"start":{"row":38,"column":31},"end":{"row":38,"column":32},"action":"insert","lines":["w"]}],[{"start":{"row":39,"column":22},"end":{"row":39,"column":23},"action":"remove","lines":["t"],"id":39},{"start":{"row":39,"column":21},"end":{"row":39,"column":22},"action":"remove","lines":["s"]},{"start":{"row":39,"column":20},"end":{"row":39,"column":21},"action":"remove","lines":["o"]},{"start":{"row":39,"column":19},"end":{"row":39,"column":20},"action":"remove","lines":["P"]},{"start":{"row":39,"column":18},"end":{"row":39,"column":19},"action":"remove","lines":["g"]},{"start":{"row":39,"column":17},"end":{"row":39,"column":18},"action":"remove","lines":["o"]},{"start":{"row":39,"column":16},"end":{"row":39,"column":17},"action":"remove","lines":["l"]},{"start":{"row":39,"column":15},"end":{"row":39,"column":16},"action":"remove","lines":["B"]}],[{"start":{"row":39,"column":15},"end":{"row":39,"column":16},"action":"insert","lines":["R"],"id":40},{"start":{"row":39,"column":16},"end":{"row":39,"column":17},"action":"insert","lines":["e"]},{"start":{"row":39,"column":17},"end":{"row":39,"column":18},"action":"insert","lines":["v"]},{"start":{"row":39,"column":18},"end":{"row":39,"column":19},"action":"insert","lines":["i"]},{"start":{"row":39,"column":19},"end":{"row":39,"column":20},"action":"insert","lines":["e"]},{"start":{"row":39,"column":20},"end":{"row":39,"column":21},"action":"insert","lines":["w"]}],[{"start":{"row":39,"column":37},"end":{"row":39,"column":38},"action":"remove","lines":["T"],"id":41},{"start":{"row":39,"column":36},"end":{"row":39,"column":37},"action":"remove","lines":["S"]},{"start":{"row":39,"column":35},"end":{"row":39,"column":36},"action":"remove","lines":["O"]},{"start":{"row":39,"column":34},"end":{"row":39,"column":35},"action":"remove","lines":["P"]}],[{"start":{"row":39,"column":34},"end":{"row":39,"column":35},"action":"insert","lines":["R"],"id":42},{"start":{"row":39,"column":35},"end":{"row":39,"column":36},"action":"insert","lines":["e"]},{"start":{"row":39,"column":36},"end":{"row":39,"column":37},"action":"insert","lines":["v"]},{"start":{"row":39,"column":37},"end":{"row":39,"column":38},"action":"insert","lines":["i"]},{"start":{"row":39,"column":38},"end":{"row":39,"column":39},"action":"insert","lines":["e"]},{"start":{"row":39,"column":39},"end":{"row":39,"column":40},"action":"insert","lines":["w"]}],[{"start":{"row":39,"column":69},"end":{"row":39,"column":70},"action":"remove","lines":["t"],"id":43},{"start":{"row":39,"column":68},"end":{"row":39,"column":69},"action":"remove","lines":["s"]},{"start":{"row":39,"column":67},"end":{"row":39,"column":68},"action":"remove","lines":["o"]},{"start":{"row":39,"column":66},"end":{"row":39,"column":67},"action":"remove","lines":["p"]}],[{"start":{"row":39,"column":66},"end":{"row":39,"column":67},"action":"insert","lines":["r"],"id":44},{"start":{"row":39,"column":67},"end":{"row":39,"column":68},"action":"insert","lines":["e"]},{"start":{"row":39,"column":68},"end":{"row":39,"column":69},"action":"insert","lines":["v"]},{"start":{"row":39,"column":69},"end":{"row":39,"column":70},"action":"insert","lines":["i"]},{"start":{"row":39,"column":70},"end":{"row":39,"column":71},"action":"insert","lines":["e"]},{"start":{"row":39,"column":71},"end":{"row":39,"column":72},"action":"insert","lines":["w"]}],[{"start":{"row":41,"column":15},"end":{"row":41,"column":16},"action":"remove","lines":["t"],"id":45},{"start":{"row":41,"column":14},"end":{"row":41,"column":15},"action":"remove","lines":["s"]},{"start":{"row":41,"column":13},"end":{"row":41,"column":14},"action":"remove","lines":["o"]},{"start":{"row":41,"column":12},"end":{"row":41,"column":13},"action":"remove","lines":["p"]}],[{"start":{"row":41,"column":12},"end":{"row":41,"column":13},"action":"insert","lines":["r"],"id":46},{"start":{"row":41,"column":13},"end":{"row":41,"column":14},"action":"insert","lines":["e"]},{"start":{"row":41,"column":14},"end":{"row":41,"column":15},"action":"insert","lines":["v"]},{"start":{"row":41,"column":15},"end":{"row":41,"column":16},"action":"insert","lines":["i"]},{"start":{"row":41,"column":16},"end":{"row":41,"column":17},"action":"insert","lines":["e"]},{"start":{"row":41,"column":17},"end":{"row":41,"column":18},"action":"insert","lines":["w"]}],[{"start":{"row":42,"column":46},"end":{"row":42,"column":47},"action":"remove","lines":["t"],"id":47},{"start":{"row":42,"column":45},"end":{"row":42,"column":46},"action":"remove","lines":["s"]},{"start":{"row":42,"column":44},"end":{"row":42,"column":45},"action":"remove","lines":["o"]},{"start":{"row":42,"column":43},"end":{"row":42,"column":44},"action":"remove","lines":["p"]}],[{"start":{"row":42,"column":43},"end":{"row":42,"column":44},"action":"insert","lines":["r"],"id":48},{"start":{"row":42,"column":44},"end":{"row":42,"column":45},"action":"insert","lines":["e"]},{"start":{"row":42,"column":45},"end":{"row":42,"column":46},"action":"insert","lines":["v"]},{"start":{"row":42,"column":46},"end":{"row":42,"column":47},"action":"insert","lines":["i"]},{"start":{"row":42,"column":47},"end":{"row":42,"column":48},"action":"insert","lines":["e"]},{"start":{"row":42,"column":48},"end":{"row":42,"column":49},"action":"insert","lines":["w"]}],[{"start":{"row":44,"column":22},"end":{"row":44,"column":23},"action":"remove","lines":["t"],"id":49},{"start":{"row":44,"column":21},"end":{"row":44,"column":22},"action":"remove","lines":["s"]},{"start":{"row":44,"column":20},"end":{"row":44,"column":21},"action":"remove","lines":["o"]},{"start":{"row":44,"column":19},"end":{"row":44,"column":20},"action":"remove","lines":["P"]},{"start":{"row":44,"column":18},"end":{"row":44,"column":19},"action":"remove","lines":["g"]},{"start":{"row":44,"column":17},"end":{"row":44,"column":18},"action":"remove","lines":["o"]},{"start":{"row":44,"column":16},"end":{"row":44,"column":17},"action":"remove","lines":["l"]},{"start":{"row":44,"column":15},"end":{"row":44,"column":16},"action":"remove","lines":["B"]}],[{"start":{"row":44,"column":15},"end":{"row":44,"column":16},"action":"insert","lines":["R"],"id":50},{"start":{"row":44,"column":16},"end":{"row":44,"column":17},"action":"insert","lines":["e"]},{"start":{"row":44,"column":17},"end":{"row":44,"column":18},"action":"insert","lines":["v"]},{"start":{"row":44,"column":18},"end":{"row":44,"column":19},"action":"insert","lines":["i"]},{"start":{"row":44,"column":19},"end":{"row":44,"column":20},"action":"insert","lines":["e"]},{"start":{"row":44,"column":20},"end":{"row":44,"column":21},"action":"insert","lines":["w"]}],[{"start":{"row":44,"column":38},"end":{"row":44,"column":39},"action":"remove","lines":["t"],"id":51},{"start":{"row":44,"column":37},"end":{"row":44,"column":38},"action":"remove","lines":["s"]},{"start":{"row":44,"column":36},"end":{"row":44,"column":37},"action":"remove","lines":["o"]},{"start":{"row":44,"column":35},"end":{"row":44,"column":36},"action":"remove","lines":["p"]}],[{"start":{"row":44,"column":35},"end":{"row":44,"column":36},"action":"insert","lines":["r"],"id":52},{"start":{"row":44,"column":36},"end":{"row":44,"column":37},"action":"insert","lines":["e"]},{"start":{"row":44,"column":37},"end":{"row":44,"column":38},"action":"insert","lines":["v"]},{"start":{"row":44,"column":38},"end":{"row":44,"column":39},"action":"insert","lines":["i"]},{"start":{"row":44,"column":39},"end":{"row":44,"column":40},"action":"insert","lines":["e"]},{"start":{"row":44,"column":40},"end":{"row":44,"column":41},"action":"insert","lines":["w"]}],[{"start":{"row":45,"column":28},"end":{"row":45,"column":36},"action":"remove","lines":["blogpost"],"id":53},{"start":{"row":45,"column":28},"end":{"row":45,"column":29},"action":"insert","lines":["r"]},{"start":{"row":45,"column":29},"end":{"row":45,"column":30},"action":"insert","lines":["e"]},{"start":{"row":45,"column":30},"end":{"row":45,"column":31},"action":"insert","lines":["v"]},{"start":{"row":45,"column":31},"end":{"row":45,"column":32},"action":"insert","lines":["i"]},{"start":{"row":45,"column":32},"end":{"row":45,"column":33},"action":"insert","lines":["e"]},{"start":{"row":45,"column":33},"end":{"row":45,"column":34},"action":"insert","lines":["w"]}],[{"start":{"row":9,"column":7},"end":{"row":9,"column":12},"action":"remove","lines":["Posts"],"id":54},{"start":{"row":9,"column":7},"end":{"row":9,"column":8},"action":"insert","lines":["R"]},{"start":{"row":9,"column":8},"end":{"row":9,"column":9},"action":"insert","lines":["e"]},{"start":{"row":9,"column":9},"end":{"row":9,"column":10},"action":"insert","lines":["v"]},{"start":{"row":9,"column":10},"end":{"row":9,"column":11},"action":"insert","lines":["i"]},{"start":{"row":9,"column":11},"end":{"row":9,"column":12},"action":"insert","lines":["e"]},{"start":{"row":9,"column":12},"end":{"row":9,"column":13},"action":"insert","lines":["w"]},{"start":{"row":9,"column":13},"end":{"row":9,"column":14},"action":"insert","lines":["s"]}],[{"start":{"row":10,"column":19},"end":{"row":10,"column":52},"action":"remove","lines":[" to the 'blogposts.html' template"],"id":55}],[{"start":{"row":9,"column":7},"end":{"row":9,"column":8},"action":"remove","lines":["R"],"id":56}],[{"start":{"row":9,"column":7},"end":{"row":9,"column":8},"action":"insert","lines":["r"],"id":57}],[{"start":{"row":20,"column":4},"end":{"row":20,"column":15},"action":"remove","lines":["Post object"],"id":59},{"start":{"row":20,"column":4},"end":{"row":20,"column":5},"action":"insert","lines":["r"]},{"start":{"row":20,"column":5},"end":{"row":20,"column":6},"action":"insert","lines":["e"]},{"start":{"row":20,"column":6},"end":{"row":20,"column":7},"action":"insert","lines":["v"]},{"start":{"row":20,"column":7},"end":{"row":20,"column":8},"action":"insert","lines":["i"]},{"start":{"row":20,"column":8},"end":{"row":20,"column":9},"action":"insert","lines":["e"]},{"start":{"row":20,"column":9},"end":{"row":20,"column":10},"action":"insert","lines":["w"]}],[{"start":{"row":20,"column":11},"end":{"row":20,"column":40},"action":"remove","lines":["based on the post ID (pk) and"],"id":60}],[{"start":{"row":20,"column":11},"end":{"row":20,"column":12},"action":"insert","lines":["a"],"id":61},{"start":{"row":20,"column":12},"end":{"row":20,"column":13},"action":"insert","lines":["n"]},{"start":{"row":20,"column":13},"end":{"row":20,"column":14},"action":"insert","lines":["d"]}],[{"start":{"row":21,"column":25},"end":{"row":21,"column":26},"action":"remove","lines":["t"],"id":62},{"start":{"row":21,"column":24},"end":{"row":21,"column":25},"action":"remove","lines":["s"]},{"start":{"row":21,"column":23},"end":{"row":21,"column":24},"action":"remove","lines":["o"]},{"start":{"row":21,"column":22},"end":{"row":21,"column":23},"action":"remove","lines":["p"]}],[{"start":{"row":21,"column":22},"end":{"row":21,"column":23},"action":"insert","lines":["r"],"id":63},{"start":{"row":21,"column":23},"end":{"row":21,"column":24},"action":"insert","lines":["e"]},{"start":{"row":21,"column":24},"end":{"row":21,"column":25},"action":"insert","lines":["v"]},{"start":{"row":21,"column":25},"end":{"row":21,"column":26},"action":"insert","lines":["i"]},{"start":{"row":21,"column":26},"end":{"row":21,"column":27},"action":"insert","lines":["e"]},{"start":{"row":21,"column":27},"end":{"row":21,"column":28},"action":"insert","lines":["w"]}],[{"start":{"row":22,"column":33},"end":{"row":22,"column":37},"action":"remove","lines":["post"],"id":64},{"start":{"row":22,"column":33},"end":{"row":22,"column":34},"action":"insert","lines":["r"]},{"start":{"row":22,"column":34},"end":{"row":22,"column":35},"action":"insert","lines":["e"]},{"start":{"row":22,"column":35},"end":{"row":22,"column":36},"action":"insert","lines":["v"]},{"start":{"row":22,"column":36},"end":{"row":22,"column":37},"action":"insert","lines":["i"]},{"start":{"row":22,"column":37},"end":{"row":22,"column":38},"action":"insert","lines":["e"]},{"start":{"row":22,"column":38},"end":{"row":22,"column":39},"action":"insert","lines":["w"]}],[{"start":{"row":32,"column":0},"end":{"row":36,"column":7},"action":"remove","lines":["    \"\"\"","    Create a view that allows us to create","    or edit a post depending if the Post ID","    is null or not","    \"\"\""],"id":65}],[{"start":{"row":13,"column":29},"end":{"row":13,"column":30},"action":"remove","lines":["d"],"id":66},{"start":{"row":13,"column":28},"end":{"row":13,"column":29},"action":"remove","lines":["e"]},{"start":{"row":13,"column":27},"end":{"row":13,"column":28},"action":"remove","lines":["h"]},{"start":{"row":13,"column":26},"end":{"row":13,"column":27},"action":"remove","lines":["s"]},{"start":{"row":13,"column":25},"end":{"row":13,"column":26},"action":"remove","lines":["i"]},{"start":{"row":13,"column":24},"end":{"row":13,"column":25},"action":"remove","lines":["l"]},{"start":{"row":13,"column":23},"end":{"row":13,"column":24},"action":"remove","lines":["b"]},{"start":{"row":13,"column":22},"end":{"row":13,"column":23},"action":"remove","lines":["u"]},{"start":{"row":13,"column":21},"end":{"row":13,"column":22},"action":"remove","lines":["p"]}],[{"start":{"row":13,"column":21},"end":{"row":13,"column":22},"action":"insert","lines":["c"],"id":67},{"start":{"row":13,"column":22},"end":{"row":13,"column":23},"action":"insert","lines":["r"]},{"start":{"row":13,"column":23},"end":{"row":13,"column":24},"action":"insert","lines":["e"]},{"start":{"row":13,"column":24},"end":{"row":13,"column":25},"action":"insert","lines":["a"]},{"start":{"row":13,"column":25},"end":{"row":13,"column":26},"action":"insert","lines":["t"]},{"start":{"row":13,"column":26},"end":{"row":13,"column":27},"action":"insert","lines":["e"]},{"start":{"row":13,"column":27},"end":{"row":13,"column":28},"action":"insert","lines":["d"]}],[{"start":{"row":12,"column":44},"end":{"row":12,"column":45},"action":"remove","lines":["d"],"id":68},{"start":{"row":12,"column":43},"end":{"row":12,"column":44},"action":"remove","lines":["e"]},{"start":{"row":12,"column":42},"end":{"row":12,"column":43},"action":"remove","lines":["h"]},{"start":{"row":12,"column":41},"end":{"row":12,"column":42},"action":"remove","lines":["s"]},{"start":{"row":12,"column":40},"end":{"row":12,"column":41},"action":"remove","lines":["i"]},{"start":{"row":12,"column":39},"end":{"row":12,"column":40},"action":"remove","lines":["l"]},{"start":{"row":12,"column":38},"end":{"row":12,"column":39},"action":"remove","lines":["b"]},{"start":{"row":12,"column":37},"end":{"row":12,"column":38},"action":"remove","lines":["u"]},{"start":{"row":12,"column":36},"end":{"row":12,"column":37},"action":"remove","lines":["p"]}],[{"start":{"row":12,"column":36},"end":{"row":12,"column":37},"action":"insert","lines":["c"],"id":69},{"start":{"row":12,"column":37},"end":{"row":12,"column":38},"action":"insert","lines":["r"]},{"start":{"row":12,"column":38},"end":{"row":12,"column":39},"action":"insert","lines":["e"]},{"start":{"row":12,"column":39},"end":{"row":12,"column":40},"action":"insert","lines":["a"]},{"start":{"row":12,"column":40},"end":{"row":12,"column":41},"action":"insert","lines":["t"]},{"start":{"row":12,"column":41},"end":{"row":12,"column":42},"action":"insert","lines":["e"]},{"start":{"row":12,"column":42},"end":{"row":12,"column":43},"action":"insert","lines":["d"]}],[{"start":{"row":14,"column":35},"end":{"row":14,"column":36},"action":"remove","lines":["t"],"id":74},{"start":{"row":14,"column":34},"end":{"row":14,"column":35},"action":"remove","lines":["s"]},{"start":{"row":14,"column":33},"end":{"row":14,"column":34},"action":"remove","lines":["o"]},{"start":{"row":14,"column":32},"end":{"row":14,"column":33},"action":"remove","lines":["p"]},{"start":{"row":14,"column":31},"end":{"row":14,"column":32},"action":"remove","lines":["g"]},{"start":{"row":14,"column":30},"end":{"row":14,"column":31},"action":"remove","lines":["o"]},{"start":{"row":14,"column":29},"end":{"row":14,"column":30},"action":"remove","lines":["l"]},{"start":{"row":14,"column":28},"end":{"row":14,"column":29},"action":"remove","lines":["b"]}],[{"start":{"row":14,"column":28},"end":{"row":14,"column":29},"action":"insert","lines":["r"],"id":75},{"start":{"row":14,"column":29},"end":{"row":14,"column":30},"action":"insert","lines":["e"]},{"start":{"row":14,"column":30},"end":{"row":14,"column":31},"action":"insert","lines":["v"]},{"start":{"row":14,"column":31},"end":{"row":14,"column":32},"action":"insert","lines":["i"]},{"start":{"row":14,"column":32},"end":{"row":14,"column":33},"action":"insert","lines":["e"]},{"start":{"row":14,"column":33},"end":{"row":14,"column":34},"action":"insert","lines":["w"]},{"start":{"row":14,"column":34},"end":{"row":14,"column":35},"action":"insert","lines":["s"]}],[{"start":{"row":14,"column":34},"end":{"row":14,"column":35},"action":"remove","lines":["s"],"id":76}],[{"start":{"row":26,"column":0},"end":{"row":26,"column":21},"action":"remove","lines":["    review.views += 1"],"id":77},{"start":{"row":25,"column":45},"end":{"row":26,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":33,"column":31},"end":{"row":33,"column":32},"action":"remove","lines":["w"],"id":78},{"start":{"row":33,"column":30},"end":{"row":33,"column":31},"action":"remove","lines":["e"]},{"start":{"row":33,"column":29},"end":{"row":33,"column":30},"action":"remove","lines":["i"]},{"start":{"row":33,"column":28},"end":{"row":33,"column":29},"action":"remove","lines":["v"]},{"start":{"row":33,"column":27},"end":{"row":33,"column":28},"action":"remove","lines":["e"]},{"start":{"row":33,"column":26},"end":{"row":33,"column":27},"action":"remove","lines":["R"]}],[{"start":{"row":33,"column":26},"end":{"row":33,"column":27},"action":"insert","lines":["P"],"id":79},{"start":{"row":33,"column":27},"end":{"row":33,"column":28},"action":"insert","lines":["O"]},{"start":{"row":33,"column":28},"end":{"row":33,"column":29},"action":"insert","lines":["S"]},{"start":{"row":33,"column":29},"end":{"row":33,"column":30},"action":"insert","lines":["T"]}],[{"start":{"row":34,"column":34},"end":{"row":34,"column":40},"action":"remove","lines":["Review"],"id":80},{"start":{"row":34,"column":34},"end":{"row":34,"column":35},"action":"insert","lines":["P"]},{"start":{"row":34,"column":35},"end":{"row":34,"column":36},"action":"insert","lines":["O"]}],[{"start":{"row":34,"column":35},"end":{"row":34,"column":36},"action":"remove","lines":["O"],"id":81}],[{"start":{"row":34,"column":35},"end":{"row":34,"column":36},"action":"insert","lines":["o"],"id":82},{"start":{"row":34,"column":36},"end":{"row":34,"column":37},"action":"insert","lines":["s"]},{"start":{"row":34,"column":37},"end":{"row":34,"column":38},"action":"insert","lines":["t"]}],[{"start":{"row":34,"column":37},"end":{"row":34,"column":38},"action":"remove","lines":["t"],"id":83},{"start":{"row":34,"column":36},"end":{"row":34,"column":37},"action":"remove","lines":["s"]},{"start":{"row":34,"column":35},"end":{"row":34,"column":36},"action":"remove","lines":["o"]}],[{"start":{"row":34,"column":35},"end":{"row":34,"column":36},"action":"insert","lines":["O"],"id":84},{"start":{"row":34,"column":36},"end":{"row":34,"column":37},"action":"insert","lines":["S"]},{"start":{"row":34,"column":37},"end":{"row":34,"column":38},"action":"insert","lines":["T"]}]]},"ace":{"folds":[],"scrolltop":262.5,"scrollleft":0,"selection":{"start":{"row":34,"column":38},"end":{"row":34,"column":38},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":96,"mode":"ace/mode/python"}},"timestamp":1587383733039,"hash":"0135b84bf60a72f0f1baf01fd6958e2a9d1cf5f3"}