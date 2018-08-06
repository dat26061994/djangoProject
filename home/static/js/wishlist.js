var BASE_URL = window.location.origin;

// Get data cart
function getwishlist() {
  $.get(BASE_URL + "/wishlist", function(data, status) {
    console.log(data);
  })
};
getwishlist();
