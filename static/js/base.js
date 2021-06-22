var article = 0;
var article_list = document.querySelectorAll("div.list-wrap");
nextSlide = () => {
    if(article >= (article_list.length - 1)){
        article_list[article].style.display="none";
        article = 0;
        article_list[article].style.display="block";
        }
    else if((article + 1) < article_list.length){
        article_list[article].style.display="none";
        article = article + 1;
        article_list[article].style.display="block";
    }

}

prevSlide = () => {
    if(article == 0){
        article_list[article].style.display="none";
        article = article + (article_list.length - 1);
        article_list[article].style.display="block";
        }
    else{
        article_list[article].style.display="none";
        article = article - 1;
        article_list[article].style.display="block";
    }
}