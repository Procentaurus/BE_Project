<?php
/* Smarty version 3.1.48, created on 2023-11-14 17:36:06
  from '/var/www/html/modules/paypal/views/templates/admin/_partials/messages/form-help-info/white-list-ip.tpl' */

/* @var Smarty_Internal_Template $_smarty_tpl */
if ($_smarty_tpl->_decodeProperties($_smarty_tpl, array (
  'version' => '3.1.48',
  'unifunc' => 'content_6553a1f6b523b5_26297527',
  'has_nocache_code' => false,
  'file_dependency' => 
  array (
    '05a0db81059e0ad62f168258fea8520e7646bec4' => 
    array (
      0 => '/var/www/html/modules/paypal/views/templates/admin/_partials/messages/form-help-info/white-list-ip.tpl',
      1 => 1699618312,
      2 => 'file',
    ),
  ),
  'includes' => 
  array (
  ),
),false)) {
function content_6553a1f6b523b5_26297527 (Smarty_Internal_Template $_smarty_tpl) {
?>
<p>
    <?php echo call_user_func_array( $_smarty_tpl->smarty->registered_plugins[Smarty::PLUGIN_FUNCTION]['l'][0], array( array('s'=>'You can test your PayPal module on production mode too. You can allow the module’s  access to a list of IP addresses. Tape the IP in the blue field for the test time and delete it after validation of the test.','mod'=>'paypal'),$_smarty_tpl ) );?>

</p>

<?php }
}
