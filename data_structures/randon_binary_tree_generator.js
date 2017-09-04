/* 
 * 
 * September 4, 2017 
 */

class Node {
	 constructor(new_name) {
         this.name = new_name;
     }

}

function makeRandomTree(node, depth) {
   // randomValue is an integer
   randomValue = Math.random() * 20;
   node.data = "" + randomValue;
   // maxDepth is likewise an integer
   maxDepth = (2 + Math.random() * 3);

   // Stop when we get deep enough. (our halt condition)
   if (depth > maxDepth) return;

   node.left = new Node();
   node.right = new Node();
   makeRandomTree(node.left, depth + 1);
   makeRandomTree(node.right, depth + 1);
}

/**
 * @param node  Node
 * @param depth integer
 */
function printTree(node, depth) {
    if (node == null) return;
    outstring = "";
    for (i = 0; i < depth; i++) {
        outstring += (i == (depth - 1) ? "|_____" : "      ");
    }

    console.log(" " + outstring + Math.round(node.data));
    printTree(node.left, depth + 1);
    printTree(node.right, depth + 1);
}

function main() {
    rootNode = new Node();
    makeRandomTree(rootNode, 0);
    printTree(rootNode, 0);
}

main();

