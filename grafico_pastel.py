<?php
  function pie() {
        $this->load->library('phpgraphlib');
	$this->load->library('phpgraphlibpie');
	$graph = new PHPGraphLibPie(330, 240);
        var $data = array(); //Lo llenan con json, xml, mysql, etc
	$graph->addData($data);
        //El name lo obtienen de alguna consulta
	$graph->setTitle('Menciones por #Hashtag : '.utf8_decode($name).'');
	$graph->setTextColor("blue");	
	$graph->setLabelTextColor('50,50,50');
	$graph->setLegendTextColor('50,50,50');
	$graph->createGraph();
   }

?>
