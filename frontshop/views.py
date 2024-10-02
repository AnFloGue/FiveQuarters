# frontshop/views.py
import logging
from django.shortcuts import render
from .services import get_order_details, get_orderitem_list
from requests.exceptions import RequestException

logger = logging.getLogger(__name__)

def order_detail(request, order_id):
    try:
        logger.info(f"Fetching order details for order_id: {order_id}")
        order_details = get_order_details(order_id)
        logger.info(f"Order details fetched: {order_details}")

        logger.info(f"Fetching order items for order_id: {order_id}")
        order_items = get_orderitem_list(order_id)  # Fetch order items for the specific order
        logger.info(f"Order items fetched: {order_items}")

        return render(request, 'frontshop/order_detail.html', {
            "order": order_details,
            "order_items": order_items  # Pass order items to the template
        })
    except RequestException as e:
        logger.error(f"Failed to fetch order details: {str(e)}")
        return render(request, 'frontshop/order_detail.html', {
            "error": f"Failed to fetch order details: {str(e)}"
        })