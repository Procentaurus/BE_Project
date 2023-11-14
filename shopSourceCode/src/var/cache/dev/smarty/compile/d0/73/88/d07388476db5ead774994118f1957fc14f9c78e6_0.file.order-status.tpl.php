<?php
/* Smarty version 3.1.48, created on 2023-11-14 17:36:07
  from '/var/www/html/modules/paypal/views/templates/admin/_partials/messages/form-help-info/order-status.tpl' */

/* @var Smarty_Internal_Template $_smarty_tpl */
if ($_smarty_tpl->_decodeProperties($_smarty_tpl, array (
  'version' => '3.1.48',
  'unifunc' => 'content_6553a1f7e0c843_63108879',
  'has_nocache_code' => false,
  'file_dependency' => 
  array (
    'd07388476db5ead774994118f1957fc14f9c78e6' => 
    array (
      0 => '/var/www/html/modules/paypal/views/templates/admin/_partials/messages/form-help-info/order-status.tpl',
      1 => 1699618312,
      2 => 'file',
    ),
  ),
  'includes' => 
  array (
  ),
),false)) {
function content_6553a1f7e0c843_63108879 (Smarty_Internal_Template $_smarty_tpl) {
?>
<p>
    <?php echo call_user_func_array( $_smarty_tpl->smarty->registered_plugins[Smarty::PLUGIN_FUNCTION]['l'][0], array( array('s'=>'You can refund the orders paid via PayPal directly via your PrestaShop BackOffice. Here, you can choose the order status that triggers the refund on PayPal. Choose the option "no actions" if you would like to change the order status without triggering the automatic refund on PayPal.','mod'=>'paypal'),$_smarty_tpl ) );?>

</p>
<p>
    <?php echo call_user_func_array( $_smarty_tpl->smarty->registered_plugins[Smarty::PLUGIN_FUNCTION]['l'][0], array( array('s'=>'You can cancel orders paid via PayPal directly via your PrestaShop BackOffice. Here, you can choose the order status that triggers the PayPal voiding of an authorized transaction on PayPal. Choose the option "no actions" if you would like to change the order status without triggering the automatic cancellation on PayPal.','mod'=>'paypal'),$_smarty_tpl ) );?>

</p>
<p>
    <?php echo call_user_func_array( $_smarty_tpl->smarty->registered_plugins[Smarty::PLUGIN_FUNCTION]['l'][0], array( array('s'=>'You are currently using the Authorize mode. It means that you separate the payment authorization from the capture of the authorized payment. For capturing the authorized payment, you have to change the order status to "payment accepted" (or to a custom status with the same meaning). Here you can choose a custom order status for accepting the order and validating transactions in Authorize mode.','mod'=>'paypal'),$_smarty_tpl ) );?>

</p>







<?php }
}
