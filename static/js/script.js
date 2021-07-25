$(document).ready(function(){
  $('[data-toggle="tooltip"]').tooltip(); 
  $('#search').submit(function(e){
    e.preventDefault();
    searchvalue = $('#search')
    $.ajax({
      'url': '/ajax/search/',
      'type': $(this).attr('method'),
      'data': searchvalue.serialize(),
      'dataType': 'json',
      'success': function(data){
        console.log(data['searchresults'])
      }
    })
  })
})