function page() {
    if (window.location.pathname == '/') {
      $('.commondimmer').dimmer('show');
    } else {
      $('.page_content').dimmer({ variation: 'inverted' }).dimmer('show');
    }

    var search = $("#search").val();
    var limit = sessionStorage.limit;
    var url = "table";
    var start = window.location.hash.substr(1);
    var data = {
        'table': sessionStorage.table,
        'search': search,
        'limit': limit,
        'start': start,
        'hot': sessionStorage.hot,
        'sellers': sessionStorage.sellers,
    };
    var get1 = $.get(url, data, function(result) {
        $("#maincontent").html(result);
        $('.dimmer').dimmer('hide');
		$("#index-bar").show()
    });

	function pagination(result) {
	    current = result.current;
	    last = result.last;
	    if (result.current <= 1) {
	        $("#minpage").hide();
	    } else {
	        $("#minpage").show();
	    }
	    if (result.current == result.last) {
	        $("#pluspage").hide();
	    } else {
	        $("#pluspage").show();
	    }
	    $("#page-current").text(result.current);
	    $("#page-last").text(result.last);
	}

    var get2 = $.getJSON('api/pagination', data, function(result) {
        pagination(result);
    });

	function finished () {}

	//I keep it with the finished, could be useful in the future
	$.when(get1, get2).done(finished);
}

function filterTable() {
    $('.commondimmer').dimmer('show');
    var search = $("#search").val();
    var limit = sessionStorage.limit;
    var url = "table";
    sessionStorage.start = 1;
    window.location.hash = 1;
    var data = {
        'table': sessionStorage.table,
        'search': search,
        'limit': limit,
        'sellers': sessionStorage.sellers,
        'hot': sessionStorage.hot
    };
    $.get(url, data, function(result) {
        $("#maincontent").html(result);
        $('.commondimmer').dimmer('hide');
    });

	function pagination(result) {
	    current = result.current;
	    last = result.last;
	    if (result.current <= 1) {
	        $("#minpage").hide();
	    } else {
	        $("#minpage").show();
	    }
	    if (result.current == result.last) {
	        $("#pluspage").hide();
	    } else {
	        $("#pluspage").show();
	    }
	    $("#page-current").text(result.current);
	    $("#page-last").text(result.last);
	}

    $.getJSON('api/pagination', data, function(result) {
        pagination(result);
    });
}

function minpage() {
    var cur = parseInt(window.location.hash.substr(1));
    var newhash = 1;
    if  (cur <= 1){
        newhash = 1;
    } else {
         newhash = cur - 1;
    }

    window.location.hash="#"+newhash;
}

function pluspage() {
    var cur = parseInt(window.location.hash.substr(1));
    var newhash = 1;
    if (cur > 1) {
        newhash = cur + 1;
    } else {
        newhash = 2;
    }

    window.location.hash="#"+newhash;
}

function sethot(s) {
    if (s == 'true') {
        sessionStorage.hot = s;
        $("#hot").addClass('blue');
        $("#all").removeClass('blue');
    } else {
        sessionStorage.hot = s;
        $("#hot").removeClass('blue');
        $("#all").addClass('blue');
    }
    filterTable();
}
function export_table(file) {
    $('.page_content').dimmer({ variation: 'inverted' }).dimmer('show');

	if (file == 'csv') {
		var format = 'csv';
	}
	if (file == 'excel') {
		var format = 'excel';
	}
    var search = $("#search").val();
    var array = [
		sessionStorage.table,
        search,
        sessionStorage.hot,
		format,
        'normal',
        sessionStorage.sellers
    ];
	var data = array.join(',');

	$('#general_export .data').attr('value', data);
    $('#general_export').submit();
	$('.page_content').dimmer('hide');
}

function b2b_export(seller, remove_user_parameter, remove_seller_parameter, coloration) {
    $('.page_content').dimmer({ variation: 'inverted' }).dimmer('show');

    var search = $("#search").val();
    var array = [
		sessionStorage.table,
        search,
        sessionStorage.hot,
		seller,
        'b2b',
        remove_user_parameter,
        remove_seller_parameter,
        coloration,
        sessionStorage.sellers
    ];
	var data = array.join(',');

	$('#b2b-export-form .data').attr('value', data);
    $('#b2b-export-form').submit();
	$('.page_content').dimmer('hide');
}

function sessionClear() {
    sessionStorage.clear();
}
function tableClear() {
    sessionStorage.table = '';
}
function showExplorer() {
    if ($('#index-bar').length==0) { //if no table_bar replace all
      document.location.href="/";
    } else {
      page();
    }
    window.history.pushState(null, '', '/');
}

function show_page(page) {
    $('.page_content').dimmer({ variation: 'inverted' }).dimmer('show');
    $.get(page, function(result) {
		    $("#index-bar").hide();
        var $response = $('<div />').html(result);
        $("#maincontent").html($response.find('.page_content')).append($response.find('.page_js'));
        window.history.pushState(null, '', '/'+page);
    });
}
