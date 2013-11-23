
var defText = 'Buscar';
function textFocus(oText)
{
if (oText.value == defText)
{
oText.value = '';
}
}
function textBlur(oText)
{
if (oText.value == '')
{
oText.value = defText;
}
}

function cargaDiv(p_Archivo,p_Div)
{
        var Text_Http;
	var xmlHttp=false;
//        var vMensaje = "Un momento por favor. Cargando la informaci&oacute;n..."
        var vMensaje = "<img src='/images/wait20trans.gif'>";

        document.getElementById(p_Div).innerHTML=vMensaje;

	if(window.XMLHttpRequest && !(window.ActiveXObject))
	{
		try
		{
			xmlHttp=new XMLHttpRequest()
		}
		catch(e)
		{
			xmlHttp=false;
		}
	}
	else if(window.ActiveXObject)
	{
		try
		{
			xmlHttp=new ActiveXObject("Msxml2.XMLHTTP");
		}
		catch(e)
		{
			try
			{
                                xmlHttp=new ActiveXObject("Microsoft.XMLHTTP");
			}
			catch(x)
			{
				xmlHttp=false;
			}
		}
	}

	xmlHttp.open("GET", p_Archivo, true);

	xmlHttp.onreadystatechange=function()
	{
		if (xmlHttp.readyState==4)
		{
			Text_Http=xmlHttp.responseText;
			
                     document.getElementById(p_Div).innerHTML=Text_Http;
		}
	}

        xmlHttp.send(null);
}
function Ir_A(p_enlace)
{        document.location.href = p_enlace;
}
function WinOpen2(url)
{        window.open(url,"BVL","toolbar=yes,directories=no,menubar=yes,status=no,resizable=yes,scrollbars=yes,scrolling=yes,width=940,height=480,left=30,top=100");
}
function getCabecera()
{        cargaDiv("/includes/cabecera.dat","divInfo");
         cargaDiv("/includes/herramientas.dat","divHerramientas");
         cargaDiv("/includes/buscador.dat","divBuscador");
         document.getElementById('divAccesos').innerHTML="";
         cargaDiv("/includes/pie.dat","divPie");
}
function getCabecera_home()
{        cargaDiv("/includes/cabecera.dat","divInfo");
         cargaDiv("/includes/herramientas.dat","divHerramientas");
         cargaDiv("/includes/buscador.dat","divBuscador");
         cargaDiv("/includes/menu_mercado.dat","divMenu");
         cargaDiv("/includes/submenu_mercado.dat","divSubmenu");
         cargaDiv("/includes/franja.dat","divFranja");
         cargaDiv("/includes/cabecera_hora.dat","divAccesos");
         cargaDiv("/includes/montos_home.dat","divMontos");
         cargaDiv("/includes/home_datos_mercado.dat","divMovimientos");
         cargaDiv("/includes/igbvl_header.dat","igbvl_header_id");
         cargaDiv("/includes/igbvl_body.dat","igbvl_body_id");
         cargaDiv("/includes/isbvl_header.dat","isbvl_header_id");
         cargaDiv("/includes/isbvl_body.dat","isbvl_body_id");
         cargaDiv("/includes/inca_header.dat","inca_header_id");
         cargaDiv("/includes/inca_body.dat","inca_body_id");
         cargaDiv("/includes/ipgc_header.dat","ibgc_header_id");
         cargaDiv("/includes/ipgc_body.dat","ibgc_body_id");
         cargaDiv("/includes/inf_Interes_home_avinteres.dat","divInfoInteres");
         cargaDiv("/includes/pie.dat","divPie");
}
function getCabecera_Mercado()
{        cargaDiv("/includes/cabecera.dat","divInfo");
         cargaDiv("/includes/herramientas.dat","divHerramientas");
         cargaDiv("/includes/buscador.dat","divBuscador");
         cargaDiv("/includes/menu_mercado.dat","divMenu");
         cargaDiv("/includes/submenu_mercado.dat","divSubmenu");
         cargaDiv("/includes/franja.dat","divFranja");
         cargaDiv("/includes/cabecera_hora.dat","divAccesos");
         cargaDiv("/includes/pie.dat","divPie");
}
function getCabecera_Mercado_Estatico()
{        cargaDiv("/includes/cabecera.dat","divInfo");
         cargaDiv("/includes/herramientas.dat","divHerramientas");
         cargaDiv("/includes/buscador.dat","divBuscador");
         cargaDiv("/includes/menu_mercado.dat","divMenu");
         cargaDiv("/includes/submenu_mercado.dat","divSubmenu");
         cargaDiv("/includes/franja.dat","divFranja");
         cargaDiv("/includes/redes_sociales.dat","divAccesos");
         cargaDiv("/includes/pie.dat","divPie");
}
function getCabecera_SusPub()
{        cargaDiv("/includes/cabecera.dat","divInfo");
         cargaDiv("/includes/herramientas.dat","divHerramientas");
         cargaDiv("/includes/buscador.dat","divBuscador");
         cargaDiv("/includes/menu_mercado.dat","divMenu");
         cargaDiv("/includes/submenu_mercado.dat","divSubmenu");
         cargaDiv("/includes/franja.dat","divFranja");
         cargaDiv("/includes/redes_sociales.dat","divAccesos");
         getBoletin_Link();
         
}
function getMenu_Izq_Empresas()
{        cargaDiv("/includes/menu_izq_empresas.dat","MenuIzq");
         getBoletin_Link();
}
function getMenu_Izq_BolsaNews()
{        cargaDiv("/includes/menu_izq_bolsanews.dat","MenuIzq");
         getBoletin_Link();
}
function getMenu_Izq_Cotizaciones()
{        cargaDiv("/includes/menu_izq_cotizaciones.dat","MenuIzq");
}
function getMenu_Izq_CotizacionesRF()
{        cargaDiv("/includes/menu_izq_cotizacionesRF.dat","MenuIzq");
}
function getMenu_Izq_Mercresumen()
{        cargaDiv("/includes/menu_izq_resumenmcdo.dat","MenuIzq");
}
function getMenu_Izq_Serv_Info()
{        cargaDiv("/includes/menu_izq_serv_info.dat","MenuIzq");
}
function getCotizacion_Empresas(p_Tabla)
{        cargaDiv("/includes/" + p_Tabla,"divCotizacion");
}
function getInf_EstadisticaGrafica(p_Nemonico)
{        var v_Nemonico = document.getElementById("id_Lista").value;
         var v_Link = "";
         document.getElementById("id_Lista").value = v_Nemonico + "|" + p_Nemonico;
         v_Link = "/jsp/Inf_EstadisticaGrafica.jsp?Listado=" + id_Lista.value;
         alert(v_Link);
         cargaDiv(v_Link,"divGrafico");
}
function getInf_Estadistica(p_Tabla,p_Nemonico)
{        getCabecera_Mercado_Estatico();
         getMenu_Izq_Empresas();
         getCotizacion_Empresas(p_Tabla);
         getBoletin_Link();
         getServiciosBVL();
//         getInf_EstadisticaGrafica(p_Nemonico);
}
function getBoletin_Link()
{        document.getElementById("divTitularBoletin").innerHTML="<h1 background-color:#154471; padding:4px 14px; font-size:12px; color:#FFFFFF; font-style:italic; margin:0>Publicaciones</h1>";
         cargaDiv("/includes/boletin_link.dat","divLinkBoletin");
}

function getBoletinAnt_Link()
{        cargaDiv("/includes/boletinAnt_link.dat","divLinkBoletinAnt");
}
function getServiciosBVL()
{        document.getElementById("divTitularServicios").innerHTML="<h1 background-color:#154471; padding:4px 14px; font-size:12px; color:#FFFFFF; font-style:italic; margin:0>Bolsa News</h1>";
         cargaDiv("/includes/serviciosBVL.dat","divServBVL");
}
function getCabecera_bursatil()
{        cargaDiv("/includes/cabecera.dat","divInfo");
         cargaDiv("/includes/herramientas.dat","divHerramientas");
         cargaDiv("/includes/buscador.dat","divBuscador");
         cargaDiv("/includes/menu_bursatil.dat","divMenu");
         cargaDiv("/includes/submenu_bursatil.dat","divSubmenu");
         cargaDiv("/includes/redes_sociales.dat","divAccesos");
         cargaDiv("/includes/pie.dat","divPie");
}
function getCabecera_acerca()
{        cargaDiv("/includes/cabecera.dat","divInfo");
         cargaDiv("/includes/herramientas.dat","divHerramientas");
         cargaDiv("/includes/buscador.dat","divBuscador");
         cargaDiv("/includes/menu_acerca.dat","divMenu");
         cargaDiv("/includes/submenu_acerca.dat","divSubmenu");
         cargaDiv("/includes/redes_sociales.dat","divAccesos");
         cargaDiv("/includes/pie.dat","divPie");
}
function getPieGoogleAnalytics()
{
         cargaDiv("/includes/piegoogle.dat","divPieGoogle");
}

function getCotizaciones(p_Tabla)
{        cargaDiv("/includes/" + p_Tabla,"divCotizaciones");
}
function get_Cotizaciones_Filtro(p_Nemonico)
{        var v_Link = "/jsp/Inf_Cotizaciones.jsp?Nemonico=" + p_Nemonico;
         cargaDiv(v_Link,"divCotizaciones");
}
function get_Cotizaciones_Empresa_Filtro(p_Nemonico)
{        var v_Link = "/jsp/Inf_Cotizaciones_Empresas.jsp?Nemonico=" + p_Nemonico;
         cargaDiv(v_Link,"divCotizaciones");
}
function getInf_Cotizaciones_Datos(p_Nemonico,p_Ini,P_Fin)
{        var v_Link = "/jsp/cotizacion.jsp?fec_inicio=" + p_Ini + "&fec_fin=" + P_Fin + "&nemonico=" + p_Nemonico;
         cargaDiv(v_Link,"divCotizaciones");
}
function get_Filtra_Noticias(p_Nemonico)
{        var v_Link = "/jsp/Inf_AvisosInteres.jsp?Nemonico=" + p_Nemonico;
         cargaDiv(v_Link,"divHHII_Noticias");
}		 
function get_Ope_Bursatiles()
{        
		 getCabecera_Mercado();
         getMenu_Izq_CotizacionesRF();
         var v_Link = "/jsp/ConsultasOperEB.jsp";
         cargaDiv(v_Link,"divOperExtrabursatiles");
		 getBoletin_Link();
		 
}
function get_Load_Noticias()
{        getCabecera_Mercado_Estatico();
         get_Noticias('6M',1,5);
         cargaDiv("/includes/menu_izq_noticias.dat","MenuIzq");
}
function get_Load_HHII()
{        getCabecera_Mercado_Estatico();
         get_HHII("TODOS","D","TODOS",1,5,"divHHII_Noticias")
         cargaDiv("/includes/menu_izq_noticias.dat","MenuIzq");
}
function get_Load_NegRV()
{        getCabecera_Mercado();
         getMenu_Izq_Cotizaciones();
         getCotizaciones("cotizaciones_busca.dat");
         getBoletin_Link();
}
function get_Load_NegRV_Filtro(p_Nemonico)
{        getCabecera_Mercado();
         getMenu_Izq_Cotizaciones();
         get_Cotizaciones_Filtro(p_Nemonico);
         chkCotizo.checked=false;
}
function get_Load_Noticias_Filtro(p_Nemonico)
{        getCabecera_Mercado_Estatico();
         getBoletin_Link();
         get_Filtra_Noticias(p_Nemonico);
}
function get_Load_Empresas_Filtro(p_Nemonico)
{        getCabecera_Mercado_Estatico();
		 getMenu_Izq_Cotizaciones();
		 get_Cotizaciones_Empresa_Filtro(p_Nemonico);
         chkCotizo.checked=false;
         
}

function get_Load_Mercresumen()
{        getCabecera_Mercado();
         getMenu_Izq_Mercresumen();
         getCotizaciones("resumen_mercado.dat");
         getBoletin_Link();
}
function get_Load_NegSector()
{        getCabecera_Mercado();
         getMenu_Izq_Cotizaciones();
         getCotizaciones("listado_sectores.dat");
         getBoletin_Link();
}
function get_Load_NegRF()
{        getCabecera_Mercado();
         getMenu_Izq_CotizacionesRF();
         getCotizaciones("cotizacionesRF.dat");
         getBoletin_Link();
}
function getInf_Cotizaciones(p_Nemonico,p_Ini,P_Fin)
{        getCabecera_Mercado_Estatico();
         getInf_Cotizaciones_Datos(p_Nemonico,p_Ini,P_Fin);
         getMenu_Izq_Empresas();
         getBoletin_Link();
         getServiciosBVL();
}
function getInf_HHII(p_Rpj,p_Rango,P_Cod_Hecho,p_Inicio,p_Fin)
{        getCabecera_Mercado_Estatico();
         get_HHII(p_Rpj,p_Rango,P_Cod_Hecho,p_Inicio,p_Fin,"divHHII_Noticias")
         getMenu_Izq_Empresas();
         getBoletin_Link();
         getServiciosBVL();
}
function getInf_Corporativa()
{        getCabecera_Mercado_Estatico();
         getMenu_Izq_Empresas();
         getBoletin_Link();
         getServiciosBVL();
}
function getInf_Financiera(p_Link)
{        getCabecera_Mercado_Estatico();
         getInf_Financiera_Empresa(p_Link);
         getMenu_Izq_Empresas();
         getBoletin_Link();
         getServiciosBVL();
}
function get_HHII(p_Rpj,p_FecIni,p_FecFin,P_Cod_Hecho,p_Inicio,p_Fin,p_Div,p_DivPaginado)
{        var v_Parametros = "?Rpj="+p_Rpj+"&Cod_Hecho="+P_Cod_Hecho+"&FechaIni="+p_FecIni+"&FechaFin="+p_FecFin+"&RangoInicio="+p_Inicio+"&RangoFin="+p_Fin;
         var vMensaje = "<img src='/images/wait20trans.gif'>";
         document.getElementById(p_Div).innerHTML=vMensaje;

         if (p_FecIni == ".")
            { alert("Ingrese la Fecha inicial");
              document.getElementById(p_Div).innerHTML="";
              return;
            }
         if (p_FecFin == ".")
            { alert("Ingrese la Fecha final");
              document.getElementById(p_Div).innerHTML="";
              return;
            }
         document.getElementById(p_Div).innerHTML = "<iframe src='/jsp/Inf_HHII.jsp" + v_Parametros + "' width='600' height='550'></iframe>";
         cargaDiv("/jsp/Inf_HHII_Paginado.jsp" + v_Parametros,p_DivPaginado);
}
function get_AvisosInteres(p_FecIni,p_FecFin,p_Inicio,p_Fin,p_Div,p_DivPaginado)
{        var v_Parametros = "?FechaIni="+p_FecIni+"&FechaFin="+p_FecFin+"&RangoInicio="+p_Inicio+"&RangoFin="+p_Fin;
         var vMensaje = "<img src='/images/wait20trans.gif'>";
         document.getElementById(p_Div).innerHTML=vMensaje;

         if (p_FecIni == ".")
            { alert("Ingrese la Fecha inicial");
              document.getElementById(p_Div).innerHTML="";
              return;
            }
         if (p_FecFin == ".")
            { alert("Ingrese la Fecha final");
              document.getElementById(p_Div).innerHTML="";
              return;
            }
         document.getElementById(p_Div).innerHTML = "<iframe src='/jsp/Inf_AvisosInteres.jsp" + v_Parametros + "' width='760' height='450'></iframe>";
         cargaDiv("/jsp/Inf_AvisosInteres_Paginado.jsp" + v_Parametros,p_DivPaginado);
}
function get_Noticias(p_FecIni,p_FecFin,p_Inicio,p_Fin,p_Div,p_DivPaginado)
{        var v_Parametros = "?FechaIni="+p_FecIni+"&FechaFin="+p_FecFin+"&RangoInicio="+p_Inicio+"&RangoFin="+p_Fin;
         var vMensaje = "<img src='/images/wait20trans.gif'>";
         document.getElementById(p_Div).innerHTML=vMensaje;

         if (p_FecIni == ".")
            { alert("Ingrese la Fecha inicial");
              document.getElementById(p_Div).innerHTML="";
              return;
            }
         if (p_FecFin == ".")
            { alert("Ingrese la Fecha final");
              document.getElementById(p_Div).innerHTML="";
              return;
            }
         document.getElementById(p_Div).innerHTML = "<iframe src='/jsp/Inf_Prensa.jsp" + v_Parametros + "' width='760' height='450'></iframe>";
         cargaDiv("/jsp/Inf_Prensa_Paginado.jsp" + v_Parametros,p_DivPaginado);
}
function get_HHII_html(p_html,p_Div,p_dat,p_DivPaginado)
{        var vMensaje = "<img src='/images/wait20trans.gif'>";
         document.getElementById(p_Div).innerHTML=vMensaje;

         cargaDiv(p_dat,p_DivPaginado);
         document.getElementById(p_Div).innerHTML = "<iframe src='" + p_html + "' width='600' height='550'></iframe>";
}
function get_Noticias_html(p_html,p_Div,p_dat,p_DivPaginado)
{        var vMensaje = "<img src='/images/wait20trans.gif'>";
         document.getElementById(p_Div).innerHTML=vMensaje;

         cargaDiv(p_dat,p_DivPaginado);
         document.getElementById(p_Div).innerHTML = "<iframe src='" + p_html + "' width='760' height='450'></iframe>";
}
function getTipo_HHII(p_Tabla)
{        cargaDiv("/includes/" + p_Tabla,"divCuadro");
}
function getInf_Financiera_Empresa(p_Link)
{        cargaDiv(p_Link,"divEEFF");
}
function setValue_ID(p_ID,p_Value)
{        window.parent.document.getElementById(p_ID).value = p_Value;
         window.parent.CB_Close(); 
}
function filtraCotizaciones(p_Valor)
{        if (p_Valor)
            getCotizaciones("cotizaciones_busca.dat");
         else
            getCotizaciones("cotizaciones_todas.dat");
}
function getLista_Empresas(p_Tabla)
{        cargaDiv("/includes/" + p_Tabla,"divTabla_Empresas");
}
function getFiltra_Empresas(p_Tabla,p_Filtro)
{
        var Text_Http;
	var xmlHttp=false;

	if(window.XMLHttpRequest && !(window.ActiveXObject))
	{
		try
		{
			xmlHttp=new XMLHttpRequest()
		}
		catch(e)
		{
			xmlHttp=false;
		}
	}
	else if(window.ActiveXObject)
	{
		try
		{
			xmlHttp=new ActiveXObject("Msxml2.XMLHTTP");
		}
		catch(e)
		{
			try
			{
                                xmlHttp=new ActiveXObject("Microsoft.XMLHTTP");
			}
			catch(x)
			{
				xmlHttp=false;
			}
		}
	}

	xmlHttp.open("GET", "/includes/" + p_Tabla, true);

	xmlHttp.onreadystatechange=function()
	{
		if (xmlHttp.readyState==4)
		{
			Text_Http=xmlHttp.responseText;
			
			if(Text_Http=="")
			{
				return;
			}
			
                     document.getElementById('divTabla_Empresas').innerHTML=filtrar_emp(Text_Http,p_Filtro.toUpperCase());;
		}
	}

        xmlHttp.send("");
}
function filtrar_emp(p_Texto,P_Filtro)
{        var v_Fila = "";
         var vTmp = "";
         var sIndex=0;
         var sIndex2=0;
         var sAux=p_Texto;
         var sSalida;
         var sInicio="class=Listado>";
         sIndex=sAux.indexOf(sInicio);
         sSalida=sAux.substring(0, sIndex+15);
         sAux=sAux.substring(sIndex+16);
         while ((sIndex=sAux.indexOf("</a></td></tr>"))!=-1)
             { v_Fila=sAux.substring(0, sIndex+14);
               vTmp=v_Fila.substring(0,sIndex-1);
               sIndex2=vTmp.indexOf(".html>")
               vTmp=vTmp.substring(sIndex2+1);
               if ((sIndex2=vTmp.indexOf(P_Filtro))!=-1)
                  sSalida+=v_Fila;
               sAux=sAux.substring(sIndex+15);
             }
         sSalida+=sAux;
         return sSalida;
}

function showEEFF(vRpj, vConsolidador, vRazoSoci,vAno,vTrimestre,vTipo1,vTipo2,vDsc_Correlativo)
{ 		 
         var v_Link = "";
		 var pFlg_Memoria;
		 document.getElementById("Ano").value = vAno;
		 document.getElementById("Trimestre").value = vTrimestre;
		 document.getElementById("Rpj").value = vRpj;
		 document.getElementById("Consolidador").value = vConsolidador;
		 document.getElementById("RazoSoci").value = vRazoSoci;
		 document.getElementById("Tipo1").value = vTipo1;
		 document.getElementById("Tipo2").value = vTipo2;
		 document.getElementById("Dsc_Correlativo").value = vDsc_Correlativo;
		 pFlg_Memoria = document.getElementById("Flg_Memoria").value;
		 v_Link = "/jsp/ShowAllEEFFxEmpresa_new.jsp?Ano=" + vAno + "&Trimestre=" + vTrimestre + "&Rpj=" + vRpj + "&Consolidador="  + vConsolidador + "&RazoSoci=" + vRazoSoci + "&Tipo1=" + vTipo1 + "&Tipo2=" + vTipo2 + "&Dsc_Correlativo=" + vDsc_Correlativo + "&Flg_Memoria=" + pFlg_Memoria;
         cargaDiv(v_Link,"divEEFF");
       }

function showEEFF2(vRpj, vAno, vTrimestre, vTipoDoc, vDsc_Correlativo, vCod_Inf)
       { 
	   
	     var v_Link = "";
		 document.getElementById("SAno").value = vAno;
		 document.getElementById("STrimestre").value = vTrimestre;
		 document.getElementById("SRpj").value = vRpj;
		 document.getElementById("STipoDoc").value = vTipoDoc;
		 document.getElementById("SInf").value = vCod_Inf;
		 document.getElementById("SDsc_Correlativo").value = vDsc_Correlativo;
		 
 		 v_Link = "/jsp/MenuPatrimonio.jsp?SAno=" + vAno + "&STrimestre=" + vTrimestre + "&SRpj=" + vRpj + "&STipoDoc="  + vTipoDoc + "&SInf=" + vCod_Inf + "&SDsc_Correlativo=" + vDsc_Correlativo;
         cargaDiv(v_Link,"divEEFF");
	   
       }
	   
	   
function SendData(pTipoDoc,pSecuencia)
		{
		  var v_Link = "";
     	  var pSRpj = "";
  		  var pSDsc_Correlativo = "";
		  var pSTipoEEFF = "";
		  var pSAno = "";
		  var pSTrimestre = "";
		  var pSInf = "";
		  
		  pSRpj = document.getElementById("SRpj").value; 
		  pSDsc_Correlativo = document.getElementById("SDsc_Correlativo").value;
		  pSTipoEEFF = document.getElementById("STipoEEFF").value; 
		  pSAno = document.getElementById("SAno").value; 
		  pSTrimestre = document.getElementById("STrimestre").value; 
		  pSInf = document.getElementById("SInf").value;
			
		  v_Link = "/jsp/ShowPatrimonio.jsp?STipoDoc=" + pTipoDoc + "&Secuencia=" + pSecuencia + "&SAno=" + pSAno + "&STrimestre=" + pSTrimestre + "&SRpj=" + pSRpj + "&STipoEEFF="  + pSTipoEEFF + "&SInf=" + pSInf + "&SDsc_Correlativo=" + pSDsc_Correlativo;
          cargaDiv(v_Link,"divEEFF");
		}	   
		
		

function Enviar_Datos(vTipoDato)
{ 
	
	 var v_Link = "";
     var sTipoInfo = "XXX";
     var sRpj = "XXX";
     var sOpciones = "XXX";
     var sRazonSocial = "XXX";
     var sDsc_Correlativo = "0000";
     var sCod_Inf = "XXX";
     var sTempEf = "XXX";
     var sCod_Hecho = "TODOS";
     var sCod_Subhecho = "TODOS";
     var sDesdeFecha = "";
     var sHastaFecha = "";
     var sTitulo = "&nbsp;";
     var sAno =  "0000";
     var sTrimestre = "XXX"; 
     var sConsolidador = "XXX";
     var sTipo1 = "XXX";
     var sTipo2 = "XXX";
     var MENU_POPUP  = "0"; 
     var sFlg_Memoria = "XXX";
     var sCod_Patrimonio = "XXX";
     var sDsc_Patrimonio = "";
     var sTipoEEFF = "";
     var sConsulta = "";
     var sVerificaAcceso = "";
     
     if (vTipoDato == "1"){
    	 if (document.InfoDataFrm.TipoInfo.value == "XXX"){ 
    		 alert('Seleccione el tipo de información.');
    		 return;
    	 }

     	document.InfoDataFrm.Rpj.value = "XXX";
     	document.InfoDataFrm.TipoRpj.value = 'XXX';
     	document.InfoDataFrm.Opciones.value = '0';
     	document.InfoDataFrm.Consulta.value = 'XXX';
     }
     
     if (vTipoDato == "2"){
    	if (document.getElementById('Rpj').value == "XXX"){ 
    		 alert('Seleccione alguna empresa.');
    		 return;
    	 }
//    	 document.InfoDataFrm.RazonSocial.value = document.getElementById('Rpj').options[document.getElementById('Rpj').selectedIndex].text;
    	 document.InfoDataFrm.RazonSocial.value = document.getElementById('Rpj').text;
    	 
     }	 
     
     if (vTipoDato == "3"){
    	if (document.getElementById('TipoRpj').value == 'XXX'){ 
    		 alert('Seleccione el Tipo de empresa.');
    		 return;
    	 }
//       	 sTempEf = document.getElementById('TipoRpj').options[document.getElementById('TipoRpj').selectedIndex].value; 
       	 sTempEf = document.getElementById('TipoRpj').value; 
    	
     }else{
    	 if (document.InfoDataFrm.TipoRpj)
           	 sTempEf = document.InfoDataFrm.TipoRpj.value; 
     }	 
     
     if (vTipoDato == "4"){
//    	 document.InfoDataFrm.Titulo.value = 'Hechos de Importancia, Otras Comunicaciones e Información de Interés Ordenados por Fecha';
    	 document.InfoDataFrm.Titulo.value = '';
//    	 document.InfoDataFrm.Tipo_HHII.value = document.InfoDataFrm.Tipo.value;
    	 document.InfoDataFrm.Consulta.value = "HHII";
     }
     
     if (vTipoDato == "5"){
    	 if (document.getElementById('Rpj').value == "XXX"){ 
    		 alert('Seleccione alguna empresa.');
    		 return;
    	 }
    	 
    	 document.InfoDataFrm.RazonSocial.value = document.getElementById('Rpj').options[document.getElementById('Rpj').selectedIndex].text;
    	 document.InfoDataFrm.RazoSoci.value = document.InfoDataFrm.RazonSocial.value;
    	 document.InfoDataFrm.Consulta.value = "EEFF";
     } 
  
     
     if (vTipoDato == "6"){
    	 
    	 if (document.getElementById('Rpj').value == "XXX")
         { alert('Seleccione algún Fondo.');
           return;
         }
    	 document.InfoDataFrm.RazonSocial.value = document.getElementById('Dsc_Patrimonio').value;
    	 document.InfoDataFrm.RazoSoci.value = document.getElementById('Dsc_Patrimonio').value;
    	 document.InfoDataFrm.Consulta.value = "EEFF";
    	 
//    	 sAno = document.getElementById('Ano').options[document.getElementById('Ano').selectedIndex].value;
//    	 sTrimestre = document.getElementById('Trimestre').options[document.getElementById('Trimestre').selectedIndex].value;
    	 sAno = document.getElementById('Ano').value;
    	 sTrimestre = document.getElementById('Trimestre').value;
    	 
    	// alert(document.InfoDataFrm.RazonSocial.value);
     }else{
    	 if (document.InfoDataFrm.Ano)
    	     	sAno = document.InfoDataFrm.Ano.value;
    	 if (document.InfoDataFrm.Trimestre)
    	     	sTrimestre = document.InfoDataFrm.Trimestre.value;
     } 
     
     
	
     if (vTipoDato == "7"){
    	 if (document.getElementById('Rpj').value == "XXX"){ 
    		 alert('Seleccione alguna empresa.');
    		 return;
    	 }
//    	 document.InfoDataFrm.RazonSocial.value = document.getElementById('Rpj').options[document.getElementById('Rpj').selectedIndex].text;
    	 document.InfoDataFrm.RazonSocial.value = document.getElementById('Rpj').text;
    	 document.InfoDataFrm.RazoSoci.value = document.getElementById('RazonSocial').value;
    	 document.InfoDataFrm.Consulta.value = "MEMO";
     }
     
     if (vTipoDato == "8"){
    	 if (document.getElementById('Rpj').value == "XXX"){ 
    		 alert('Seleccione algún Fondo.');
    	 	 return;
    	 }
    	 
    	 document.InfoDataFrm.RazonSocial.value = document.getElementById('Dsc_Patrimonio').value;
    	 document.InfoDataFrm.RazoSoci.value = document.getElementById('Dsc_Patrimonio').value;
    	 document.InfoDataFrm.Consulta.value = "MEMO";
     }	 
     
   
	 if (document.InfoDataFrm.Rpj)
    	 sRpj = document.InfoDataFrm.Rpj.value;
     
     if (document.InfoDataFrm.Titulo)
    	 sTitulo = document.InfoDataFrm.Titulo.value;
     if (document.InfoDataFrm.Consulta)
    	 sConsulta = document.InfoDataFrm.Consulta.value;
 

     if (document.InfoDataFrm.TipoInfo){
    	 sTipoInfo = document.getElementById('TipoInfo').options[document.getElementById('TipoInfo').selectedIndex].value;
    	 //alert(sTipoInfo);
     } 
     
     
 
     
     if (document.InfoDataFrm.Opciones)
    	 sOpciones = document.InfoDataFrm.Opciones.value;
     if (document.InfoDataFrm.VerificaAcceso)
    	 sVerificaAcceso = document.InfoDataFrm.VerificaAcceso.value;

         
     if (document.InfoDataFrm.RazonSocial)
    	 sRazonSocial = document.InfoDataFrm.RazonSocial.value;
     if (document.InfoDataFrm.Dsc_Correlativo)
    	 sDsc_Correlativo = document.InfoDataFrm.Dsc_Correlativo.value;
     if (document.InfoDataFrm.SInf)
     	sCod_Inf = document.InfoDataFrm.SInf.value;
     if (document.InfoDataFrm.Cod_Subhecho)
     	sCod_Subhecho = document.InfoDataFrm.Cod_Subhecho.value;
     if (document.InfoDataFrm.DFecha)
     	sDesdeFecha = document.InfoDataFrm.DFecha.value;
     if (document.InfoDataFrm.AFecha)
     	sHastaFecha = document.InfoDataFrm.AFecha.value;
    
     if (document.InfoDataFrm.Consolidador)
     	sConsolidador = document.InfoDataFrm.Consolidador.value;
     if (document.InfoDataFrm.RazoSoci)
     	sRazoSociConsolidador = document.InfoDataFrm.RazoSoci.value;
     if (document.InfoDataFrm.Tipo1)
     	sTipo1 = document.InfoDataFrm.Tipo1.value;
     if (document.InfoDataFrm.Tipo2)
     	sTipo2 = document.InfoDataFrm.Tipo2.value;
     if (document.InfoDataFrm.MENU_POPUP)
     	MENU_POPUP  = document.InfoDataFrm.MENU_POPUP.value;
     if (document.InfoDataFrm.Flg_Memoria)
     	sFlg_Memoria = document.InfoDataFrm.Flg_Memoria.value;
     if (document.InfoDataFrm.Cod_Patrimonio)
     	sCod_Patrimonio = document.InfoDataFrm.Cod_Patrimonio.value;
     if (document.InfoDataFrm.Dsc_Patrimonio)
     	sDsc_Patrimonio = document.InfoDataFrm.Dsc_Patrimonio.value;
     if (document.InfoDataFrm.TipoEEFF)
     	sTipoEEFF = document.InfoDataFrm.TipoEEFF.value;
         
	 v_Link = "/jsp/info_emp.jsp?TipoInfo=" + sTipoInfo + "&Rpj=" + sRpj + "&Opciones=" + sOpciones + "&RazonSocial=" + sRazonSocial + "&Dsc_Correlativo=" +  sDsc_Correlativo + "&SInf=" + sCod_Inf;
	 v_Link = v_Link +  "&TipoRpj=" + sTempEf + "&Cod_Subhecho=" + sCod_Subhecho + "&DFecha=" + sDesdeFecha + "&AFecha=" + sHastaFecha + "&Titulo=" + sTitulo; 
	 v_Link = v_Link + "&Ano=" + sAno + "&Trimestre=" + sTrimestre + "&Consolidador=" + sConsolidador + "&RazoSoci=" + sRazonSocial + "&Tipo1=" + sTipo1;
	 v_Link = v_Link + "&Tipo2=" + sTipo2 + "&MENU_POPUP=" + MENU_POPUP + "&Flg_Memoria=" + sFlg_Memoria + "&Cod_Patrimonio=" + sCod_Patrimonio+ "&Dsc_Patrimonio=" + sDsc_Patrimonio;
	 v_Link = v_Link + "&TipoEEFF=" + sTipoEEFF + "&Consulta=" + sConsulta + "&VerificaAcceso=" + sVerificaAcceso;

//	 alert(v_Link);
	 cargaDiv(v_Link,"divEEFF");

}

function open_new_window2(sFiltro)
{ col_win = window.open("/jsp/ListPatrimonios.jsp?SInf=" + sFiltro, "MenuTipoInfo007", "menubar=no,scrollbars=yes,toolbar=no,resizable=yes,width=420,height=300");
}

function open_new_window()
{ 
  var Cod = "TODOS";
  col_win = window.open("/jsp/AsuntosHHII.jsp?Cod_Hecho=" + Cod,"Asuntos","menubar=no,scrollbars=yes,toolbar=no,resizable=yes,width=420,height=300");
}

function getAgenteMila()
{        document.getElementById("divTitularAgente").innerHTML="<h1 background-color:#154471; padding:4px 14px; font-size:12px; color:#FFFFFF; font-style:italic; margin:0>Nuevo</h1>";
         cargaDiv("/includes/agente_Mila.dat","divAgenteMila");
}