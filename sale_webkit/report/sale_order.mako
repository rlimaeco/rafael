<html>
<head>
     <style type="text/css">
                ${css}
            </style>
</head>
<body>
    %for o in objects:
    <% setLang(o.partner_id.lang) %>
        
    <table class="shipping_address" width="100%">
          <tr>
            <td width="70%">
                    <b>${_("Shipping address :")}</b><br>
                    ${ (o.partner_shipping_id and o.partner_shipping_id.name) or '' }</br>
                    ${(o.partner_shipping_id.legal_name) or ''}<br>

                    
                   ${o.partner_shipping_id.street or ''}, ${(o.partner_shipping_id.number) or ''|entity}<br>
                %if o.partner_shipping_id.street2 :
                    ${o.partner_shipping_id.street2 or ''|entity}<br>
                %endif
                  
                  ${o.partner_shipping_id.zip or ''} ${o.partner_shipping_id.city or ''} - ${o.partner_shipping_id.state_id.code or ''}<br>
                
              </td>
             
             </tr>
             <tr>
                 <td> 
                  <b>${_("Invoice address :")}</b><br>
                     ${ (o.partner_invoice_id and o.partner_invoice_id.name) or '' }</br>
                     ${ (o.partner_invoice_id.legal_name) or '' }</br>
                     ${o.partner_invoice_id.street or ''|entity}, ${o.partner_invoice_id.number or ''|entity}</br>  
                    %if o.partner_invoice_id.street2 :
                      ${o.partner_invoice_id.street2 or ''|entity}</br>
                    %endif
                ${o.partner_invoice_id.zip or ''|entity} ${o.partner_invoice_id.city or ''|entity} - ${o.partner_invoice_id.state_id.code or ''|entity}</br>
                 </td>
              </tr>
    </table>
    
    %if o.state not in ['draft','sent'] or '':
      <p class="title" align="center"><b> ${_("Pedido N°") } ${ o.name } - Data: ${o.date_order}</b></p>
    %endif
    %if o.state in ['draft','sent'] or '':
      <p class="title" align="center"><b>${_("Cotação N°") } ${ o.name } - Data: ${o.date_order}</b></p>
    %endif
    
    <table class="basic_table" >
      <tr>
        <td width="25%"></br>
          <b>${_("Your Reference")}</b>
        </td>
        <td width="25%"></br>
        %if o.state in ['draft','sent'] :
          <b>${ o.state in ['draft','sent'] or ''|entity } ${_("Date Ordered")}</b>
        %endif
        %if o.state not in ['draft','sent'] :
          <b>${ o.state not in ['draft','sent'] or ''|entity } ${_("Quotation Date")}</b>
        %endif
        </td></br>
        <td width="25%"></br>
          <b>${_("Salesperson")}</b>
        </td>
        <td width="25%"></br>
          <b>${_("Payment Term")}</b>
        </td>
      </tr>
    
      <tr>
        <td width="25%">
        %if o.client_order_ref :
          ${ o.client_order_ref or ''|entity}
        %endif
        </td>
        <td width="25%">
          ${ formatLang(o.date_order,date = True) }
        </td>
        <td width="25%">
          ${ (o.user_id and o.user_id.name) or '' }
        </td>
        <td width="25%">
          ${ (o.payment_term and o.payment_term.name) or '' }
        </td>
      </tr>
    </table>
     </br>
    <table class="tr_bottom_line">
      <tr>
        <td width="50%">
          <b>${_("Description")}</b>
        </td>
        <td width="10%">
          <b>${_("Quantity")}</b>
        </td>
        <td width="10%" align="right">
          <b>${_("Unit Price")}</b>
        </td>
        <td width="15%" align="right">
          <b>${_("Disc.(%)")}</b>
        </td>
        <td width="15%" align="right">
          <b>${_("Price")}</b>
        </td>
      </tr>
    </table>
    
    
    %for line in o.order_line:
      <table class="tr_bottom_line_dark_grey">
        <tr>
          <td width="50%"> 
            ${ format(line.name) }
          </td>
          <td width="12%">
            ${ formatLang(line.product_uos and line.product_uos_qty or line.product_uom_qty) } ${ line.product_uos and line.product_uos.name or line.product_uom.name }
          </td>
          <td width="8%" >
            ${ formatLang(line.price_unit , digits=get_digits(dp='Product Price')) }
          </td>
          <td width="15%">
            ${ show_discount(user.id) and formatLang(line.discount, digits=get_digits(dp='Discount')) or ''|entity }
          </td>
          <td width="15%" style="text-align:right">
            ${ formatLang(line.price_subtotal, digits=get_digits(dp='Account'), currency_obj=o.pricelist_id.currency_id) }
          </td>
        </tr>
      </table>
    %endfor
      <table width="100%">
        <tr>
          <td width="70%">
          </td>
          <td width="30%">
            <table class="tr_top">
              <tr>
                <td >
                  ${_("Vlr. Bruto :")}
                </td>
                <td width="40%" style="text-align:right">
                  ${ formatLang(o.amount_gross, dp='Account', currency_obj=o.pricelist_id.currency_id) }
                </td>
              </tr>
              <tr>
                <td >
                  ${_("Valor líquido :")}
                </td>
                <td width="40%" style="text-align:right">
                  ${ formatLang(o.amount_untaxed, dp='Account', currency_obj=o.pricelist_id.currency_id) }
                </td>
              </tr>
              <tr>
                <td >
                  <b>${_("Frete :")}</b>
                </td>
                <td width="40%" style="text-align:right"> 
                  ${ formatLang(o.amount_freight, dp='Account', currency_obj=o.pricelist_id.currency_id) }
                </td>
              </tr>
              <tr>
                <td >
                  <b>${_("Seguro :")}</b>
                </td>
                <td width="40%" style="text-align:right"> 
                  ${ formatLang(o.amount_insurance, dp='Account', currency_obj=o.pricelist_id.currency_id) }
                </td>
              </tr>
              <tr>
                <td >
                  <b>${_("Outros Custos :")}</b>
                </td>
                <td width="40%" style="text-align:right"> 
                  ${ formatLang(o.amount_costs, dp='Account', currency_obj=o.pricelist_id.currency_id) }
                </td>
              </tr>
              <tr>
                <td >
                  ${_("Impostos :")}
                </td>
                <td width="40%" style="text-align:right"> 
                  ${ formatLang(o.amount_tax, dp='Account', currency_obj=o.pricelist_id.currency_id) }
                </td>
              </tr>
            </table>
          </td>
        </tr>
        <tr>
          <td></td>
          <td>
            <table class="tr_top">
              <tr>
                <td>
                  <b>${_("Total :")}</b>
                </td>
                <td align="right">
                  <b>${ formatLang(o.amount_total, dp='Account', currency_obj=o.pricelist_id.currency_id) }</b>
                </td>
            </tr>
          </table>
         </td>
      </tr>
      </table>
      </br>
      <p class="td_f12">${ (format(o.note or '') ) }
      
       <p style="page-break-after:always"></p>
      %endfor
</body>
</html>
