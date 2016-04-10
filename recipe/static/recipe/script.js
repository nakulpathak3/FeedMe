$(document).ready(function(){
    var newInputCount = 0;

    function newTFWListner(){
        $(".text-field-wrapper").click(
            function(){
                $(".selected").removeClass("selected");
                $(this).addClass("selected");
                newTFWListner();
            }
        );
    }

    function newLCListener(){
        $(".last").click(
            function(){
                if($(this).hasClass("last")){
                    $(this).removeClass("last");
                    ++newInputCount;
                    var newInput = '<div class="text-field-wrapper last"><label for="ingredient">Ingredient</label><input class="text-field" type="text" name="ingredient' + newInputCount + '">';
                    $(this).after(newInput);
                    newLCListener();
                }
            }
        );
    }

    newLCListener();
    newTFWListner();

    $('.recipes-wrapper').find('.recipe').hide();

    $('.recipes-wrapper').click(function() {
        var el = $(this).find('.recipe');
        if(el.hasClass("off")){
            el.slideDown();
            el.removeClass("off");
            el.addClass("on");
        }
        else if(el.hasClass("on")){
            el.slideUp();
            el.removeClass("on");
            el.addClass("off");
        }
    });

});
