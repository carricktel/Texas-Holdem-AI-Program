

var Card = function(NumVal,Suit,ID,Img){
    this.NumVal = NumVal;
    this.Suit = Suit;
    this.ID = ID;

    this.Img = new Image();
    this.Img.src = Img;
}

var Table = function(AI_Stack,Player_Stack,SB){
    this.AI_Stack = AI_Stack;
    this.Player_Stack = Player_Stack;
    this.SB = SB;

    this.Winner = 0;
    this.BB = 2*this.SB;
    this.Round = 1;
    this.Dealer_Button = 1;
    this.Action_To = this.Dealer_Button;
    this.Community_Cards = [];
    this.Player_Cards = [];
    this.AI_Cards = [];
    this.Player_Best_Cards = [];
    this.Pot_Stack = 0;
    this.Action_To = [0,"",0];
    this.Raise_Pot = 0;
    this.New_Hand = false;
    this.Deck = new Array(new Card(2,"Hearts",1,"../static/2ofHearts.png"),new Card(3,"Hearts",2,"../static/3ofHearts.png"),
 						  new Card(4,"Hearts",3,"../static/4ofHearts.png"),new Card(5,"Hearts",4,"../static/5ofHearts.png"),
						  new Card(6,"Hearts",5,"../static/6ofHearts.png"),new Card(7,"Hearts",6,"../static/7ofHearts.png"),
						  new Card(8,"Hearts",7,"../static/8ofHearts.png"),new Card(9,"Hearts",8,"../static/9ofHearts.png"),
						  new Card(10,"Hearts",9,"../static/TofHearts.png"),new Card(11,"Hearts",10,"../static/JofHearts.png"),
						  new Card(12,"Hearts",11,"../static/QofHearts.png"),new Card(13,"Hearts",12,"../static/KofHearts.png"),
						  new Card(14,"Hearts",13,"../static/AofHearts.png"),new Card(2,"Diamonds",14,"../static/2ofDiamonds.png"),
	 					  new Card(3,"Diamonds",15,"../static/3ofDiamonds.png"),new Card(4,"Diamonds",16,"../static/4ofDiamonds.png"),
						  new Card(5,"Diamonds",17,"../static/5ofDiamonds.png"),new Card(6,"Diamonds",18,"../static/6ofDiamonds.png"),
						  new Card(7,"Diamonds",19,"../static/7ofDiamonds.png"),new Card(8,"Diamonds",20,"../static/8ofDiamonds.png"),
						  new Card(3,"Spades",41,"../static/3ofSpades.png"),new Card(4,"Spades",42,"../static/4ofSpades.png"),
						  new Card(5,"Spades",43,"../static/5ofSpades.png"),new Card(6,"Spades",44,"../static/6ofSpades.png"),
						  new Card(7,"Spades",45,"../static/7ofSpades.png"),new Card(8,"Spades",46,"../static/8ofSpades.png"),
						  new Card(9,"Spades",47,"../static/9ofSpades.png"),new Card(10,"Spades",48,"../static/TofSpades.png"),
						  new Card(11,"Spades",49,"../static/JofSpades.png"),new Card(12,"Spades",50,"../static/QofSpades.png"),
						  new Card(13,"Spades",51,"../static/KofSpades.png"),new Card(14,"Spades",52,"../static/AofSpades.png"),
						  new Card(4,"Clubs",29,"../static/4ofClubs.png"),new Card(5,"Clubs",30,"../static/5ofClubs.png"),
						  new Card(6,"Clubs",31,"../static/6ofClubs.png"),new Card(7,"Clubs",32,"../static/7ofClubs.png"),
						  new Card(8,"Clubs",33,"../static/8ofClubs.png"),new Card(9,"Clubs",34,"../static/9ofClubs.png"),
						  new Card(10,"Clubs",35,"../static/TofClubs.png"),new Card(11,"Clubs",36,"../static/JofClubs.png"),
						  new Card(12,"Clubs",37,"../static/QofClubs.png"),new Card(13,"Clubs",38,"../static/KofClubs.png"),
						  new Card(14,"Clubs",39,"../static/AofClubs.png"),new Card(2,"Spades",40,"../static/2ofSpades.png"),
						  new Card(11,"Diamonds",23,"../static/JofDiamonds.png"),new Card(12,"Diamonds",24,"../static/QofDiamonds.png"),
						  new Card(13,"Diamonds",25,"../static/KofDiamonds.png"),new Card(14,"Diamonds",26,"../static/AofDiamonds.png"),
						  new Card(2,"Clubs",27,"../static/2ofClubs.png"),new Card(3,"Clubs",28,"../static/3ofClubs.png"),
						  new Card(9,"Diamonds",21,"../static/9ofDiamonds.png"),new Card(10,"Diamonds",22,"../static/TofDiamonds.png"));
						  
						  
}
function init(aicard1_ID,aicard2_ID,plyrcard1_ID,plyrcard2_ID,comcard1_ID,comcard2_ID,comcard3_ID,comcard4_ID,comcard5_ID,com_p,ai_p,plyr_p) {
    var table = new Table(0,0,0);
//    var card = new Card(2,"Hearts",1,"2ofHearts.png");
    var canvas = document.getElementById('myCanvas');
    var context = canvas.getContext('2d');
    var pokertable = new Image();
    pokertable.src = '../static/pokertable.png';
	var cardback = new Image();
	cardback.src = '../static/backofcard.png';

    var AofClubs = new Image();
    AofClubs.src = '../static/AofClubs.png';

     pokertable.onload = function(){
        context.drawImage(pokertable,200,0);
 		context.drawImage(cardback,340,10);
		context.drawImage(cardback,400,10);
		var c;
		for(c = 0; c<table.Deck.length; c++){
			if (table.Deck[c].ID == plyrcard1_ID){
				context.drawImage(table.Deck[c].Img,340,188);}
			if (table.Deck[c].ID == plyrcard2_ID){
				context.drawImage(table.Deck[c].Img,400,188);}
			if (table.Deck[c].ID == comcard1_ID){
				context.drawImage(table.Deck[c].Img,280,100);}
			if (table.Deck[c].ID == comcard2_ID){
				context.drawImage(table.Deck[c].Img,340,100);}
			if (table.Deck[c].ID == comcard3_ID){
				context.drawImage(table.Deck[c].Img,400,100);}
			if (table.Deck[c].ID == comcard4_ID){
				context.drawImage(table.Deck[c].Img,460,100);}
			if (table.Deck[c].ID == comcard5_ID){
				context.drawImage(table.Deck[c].Img,520,100);}
			if (table.Deck[c].ID == aicard1_ID){
				context.drawImage(table.Deck[c].Img,340,10);}
			if (table.Deck[c].ID == aicard2_ID){
				context.drawImage(table.Deck[c].Img,400,10);}
		}
		context.font="30px Georgia";
		context.fillText(com_p,230,142);
		context.fillText(ai_p,230,67);
		context.fillText(plyr_p,230,222);
} 
}
