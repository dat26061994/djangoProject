  $(document).ready(function() {

    var ShowForm = function() {
      var btn = $(this);
      $.ajax({
        url: btn.attr("data-url"),
        type: 'get',
        dataType: 'json',
        beforeSend: function() {
          $('#show_modal').modal('show');
        },
        success: function(data) {
          console.log(data);
          $('#show_modal .modal-content').html(data.html_form);
        }
      });
    };

    // Show Form Modal Product

    $(".show_modal_pr").click(function(e) {
      var btn = $(this);
      $.ajax({
        url: btn.attr("data-url"),
        type: 'get',
        dataType: 'json',
        beforeSend: function() {
          $('#show_modal_pr123').modal('show');
        },
        success: function(data) {
          console.log(data);
          $('#show_modal_pr123 .modal-dialog .modal-content').html(data.html);
          $('.previews a').click(function() {
            var largeImage = $(this).attr('data-full');
            $('.selected').removeClass();
            $(this).addClass('selected');
            $('.full img').hide();
            $('.full img').attr('src', largeImage);
            $('.full img').fadeIn();
          }); // closing the listening on a click
          $('.full img').on('click', function() {
            var modalImage = $(this).attr('src');
            $.fancybox.open(modalImage);
          });
          $('#content-pr').on("submit", ".addcart", SaveForm)
        }
      });

    })


    var SaveForm = function() {
      console.log('123');
      var form = $(this);
      $.ajax({
        url: form.attr('data-url'),
        data: form.serialize(),
        type: form.attr('method'),
        dataType: 'json',
        success: function(data) {
          console.log(data);
          $('#show_modal').modal('hide');
          if (data.success) {
            if (data.wishlist) {
              $('#wishlist-table tbody').html(data.wishlist);
            }
            if (data.cart) {
              $('.dialog-cart .modal-content').html(data.cart);
              $('.show_cart').attr('data-notify', data.count);
              console.log($('.show_cart').attr('data-notify'));
            }
            if (data.review) {
              $('#show_review').html(data.review);
              $('.count_review').html(data.count);
            }
            swal("Success!", data.message, "success");
          } else {
            swal("Error!", data.message, "error");
          }
        }
      })
      return false;
    }
    var showPrDetail = function() {
      console.log(123);
      var btn = $(this);
      $.ajax({
        url: btn.attr("data-url"),
        type: 'get',
        dataType: 'json',
        success: function(data) {
          console.log(data);
          $('#show_modal .pr_show_modal').html(data.html);
        }
      });
    };

    $('#act_page_review_1').addClass("active-pagination1");
    var show_cont_review = function() {
      console.log(123);
      var btn = $(this)
      $.ajax({
        url: btn.attr("data-url"),
        type: 'get',
        dataType: 'json',
        success: function(data) {
          console.log(data);
          $('#show_review').html(data.review);
          console.log(btn.attr('value'));
          for (var i = 1; i <= data.totalpage; i++) {
            if (i == data.page) {
              $('#act_page_review_' + i).addClass("active-pagination1");
            } else {
              $('#act_page_review_' + i).removeClass("active-pagination1");
            }
          }
          if (data.page == 1) {
            $('.previous').addClass("dis-none-impor");
          } else {
            $('.previous').removeClass("dis-none-impor");
            $('.previous').attr('data-url', '?page=' + String(data.page - 1))
          }
          if (data.page == data.totalpage) {
            $('.next').addClass("dis-none-impor");
          } else {
            $('.next').removeClass("dis-none-impor");
            $('.next').attr('data-url', '?page=' + String(data.page + 1))
          }
        }
      });
    }
    var SaveCoupouns = function() {
      var form = $(this);
      $.ajax({
        url: form.attr("data-url"),
        type: 'post',
        data:form.serialize(),
        dataType: 'json',
        success: function(data) {
          console.log(data);
        }
      });
    }
    // $('.btn_update_coupouns').on("click",function() {
    //   var btn = $(this);
    //   var coupouns = $('#coupons').val()
    //   $.ajax({
    //     url: btn.attr("data-url"),
    //     type: 'post',
    //     data:{
    //       coupouns:coupouns
    //     },
    //     dataType: 'json',
    //     success: function(data) {
    //       console.log(data);
    //     }
    //   });
    // })
    $('.pagination').on("click", ".act_page_review", show_cont_review);
    $('#review-pg').on("submit", ".review-form", SaveForm)
    // $('#coupons').on("submit", ".update_coupouns", SaveCoupouns)
    // $('#viewmore').on('click','.show_modal_pr',showPrDetail)
    $('.show_cart').on("click", function() {
      $('#show_modal_cart').modal('show');
    })
    $('#wishlist-table').on("click", ".show-form-delete", ShowForm);
    $('#show_modal').on("submit", ".delete-form", SaveForm)
    $('.add-wishlist').on("submit", SaveForm)



    $("#menu-toggle").click(function(e) {
      e.preventDefault();
      $("#wrapper").toggleClass("active");
    });
    $('#messageProfile').show().delay(5000).fadeOut();
    $('#id_gender').addClass('form-control')


    $('input[name=price-pr]').change(function() {
      $('#form-search-price').submit();
    });
    var BASE_URL = window.location.origin;

    $('.js-pscroll').each(function() {
      $(this).css('position', 'relative');
      $(this).css('overflow', 'hidden');
      var ps = new PerfectScrollbar(this, {
        wheelSpeed: 1,
        scrollingThreshold: 1000,
        wheelPropagation: false,
      });

      $(window).on('resize', function() {
        ps.update();
      })
    });

  });
