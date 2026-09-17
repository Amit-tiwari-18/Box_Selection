from django.shortcuts import render
from .models import Product, Box


def home(request):
    return render(request, 'home.html')


def recommend_box(request):
    products = Product.objects.all()

    if request.method == 'POST':
        product_id = request.POST.get('product')
        product = Product.objects.get(id=product_id)

        suitable_boxes = []

        for box in Box.objects.all():

            # Check weight
            weight_ok = product.weight <= box.max_weight

            # Sort dimensions for flexible orientation
            product_dimensions = sorted([
                product.length,
                product.width,
                product.height
            ])

            box_dimensions = sorted([
                box.length,
                box.width,
                box.height
            ])

            # Check dimensions
            dimensions_ok = all(
                p <= b
                for p, b in zip(product_dimensions, box_dimensions)
            )

            if weight_ok and dimensions_ok:
                suitable_boxes.append(box)

        # Select the lowest-cost suitable box
        suitable_boxes.sort(key=lambda box: box.cost)

        recommended_box = (
            suitable_boxes[0] if suitable_boxes else None
        )

        return render(
            request,
            'result.html',
            {
                'product': product,
                'recommended_box': recommended_box,
                'suitable_boxes': suitable_boxes,
            }
        )

    return render(
        request,
        'product.html',
        {'products': products}
    )