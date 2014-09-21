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
});