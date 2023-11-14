<?php
/* Smarty version 3.1.48, created on 2023-11-14 17:36:07
  from '/var/www/html/modules/paypal/views/templates/admin/_partials/statusBlock.tpl' */

/* @var Smarty_Internal_Template $_smarty_tpl */
if ($_smarty_tpl->_decodeProperties($_smarty_tpl, array (
  'version' => '3.1.48',
  'unifunc' => 'content_6553a1f7e5e4b7_99784578',
  'has_nocache_code' => false,
  'file_dependency' => 
  array (
    'dddc083f19d237878bd6ff06c9baaf246ee2da0a' => 
    array (
      0 => '/var/www/html/modules/paypal/views/templates/admin/_partials/statusBlock.tpl',
      1 => 1699618312,
      2 => 'file',
    ),
  ),
  'includes' => 
  array (
  ),
),false)) {
function content_6553a1f7e5e4b7_99784578 (Smarty_Internal_Template $_smarty_tpl) {
?><div class="row pb-3 h-100">
  <div class="col-12 col-lg-9 col-xl-8 pb-4">
    <p>
      <?php echo call_user_func_array( $_smarty_tpl->smarty->registered_plugins[Smarty::PLUGIN_FUNCTION]['l'][0], array( array('s'=>'Merchant Country:','mod'=>'paypal'),$_smarty_tpl ) );?>
 <b><?php echo call_user_func_array($_smarty_tpl->registered_plugins[ 'modifier' ][ 'escape' ][ 0 ], array( $_smarty_tpl->tpl_vars['vars']->value['merchantCountry'],'htmlall','UTF-8' ));?>
</b>
    </p>

    <p>
      <?php ob_start();
echo call_user_func_array( $_smarty_tpl->smarty->registered_plugins[Smarty::PLUGIN_FUNCTION]['l'][0], array( array('s'=>'To  modify country: [a @href1@]International > Localization[/a]','mod'=>'paypal'),$_smarty_tpl ) );
$_prefixVariable12 = ob_get_clean();
ob_start();
echo $_smarty_tpl->tpl_vars['vars']->value['localizationUrl'];
$_prefixVariable13 = ob_get_clean();
ob_start();
echo 'target="blank"';
$_prefixVariable14 = ob_get_clean();
echo smarty_modifier_paypalreplace($_prefixVariable12,array('@href1@'=>$_prefixVariable13,'@target@'=>$_prefixVariable14));?>

    </p>

    <ul class="list-unstyled mb-0">
      <li class="d-flex mb-1">
        <?php $_smarty_tpl->_subTemplateRender(($_smarty_tpl->tpl_vars['moduleFullDir']->value).("/views/templates/admin/_partials/icon-status.tpl"), $_smarty_tpl->cache_id, $_smarty_tpl->compile_id, 0, $_smarty_tpl->cache_lifetime, array('isSuccess'=>(($tmp = @$_smarty_tpl->tpl_vars['vars']->value['sslActivated'])===null||$tmp==='' ? false : $tmp)), 0, true);
?>
        <?php if ((($tmp = @$_smarty_tpl->tpl_vars['vars']->value['sslActivated'])===null||$tmp==='' ? false : $tmp)) {?>
          <?php echo call_user_func_array( $_smarty_tpl->smarty->registered_plugins[Smarty::PLUGIN_FUNCTION]['l'][0], array( array('s'=>'SSL enabled.','mod'=>'paypal'),$_smarty_tpl ) );?>

        <?php } else { ?>
          <?php echo call_user_func_array( $_smarty_tpl->smarty->registered_plugins[Smarty::PLUGIN_FUNCTION]['l'][0], array( array('s'=>'SSL should be enabled on your website.','mod'=>'paypal'),$_smarty_tpl ) );?>

        <?php }?>
      </li>

      <?php if ((($tmp = @$_smarty_tpl->tpl_vars['vars']->value['tlsVersion'])===null||$tmp==='' ? false : $tmp)) {?>
        <li class="d-flex mb-1">
          <?php $_smarty_tpl->_subTemplateRender(($_smarty_tpl->tpl_vars['moduleFullDir']->value).("/views/templates/admin/_partials/icon-status.tpl"), $_smarty_tpl->cache_id, $_smarty_tpl->compile_id, 0, $_smarty_tpl->cache_lifetime, array('isSuccess'=>((($tmp = @$_smarty_tpl->tpl_vars['vars']->value['tlsVersion'])===null||$tmp==='' ? false : $tmp) && $_smarty_tpl->tpl_vars['vars']->value['tlsVersion']['status'])), 0, true);
?>
          <?php if ((($tmp = @$_smarty_tpl->tpl_vars['vars']->value['tlsVersion'])===null||$tmp==='' ? false : $tmp) && $_smarty_tpl->tpl_vars['vars']->value['tlsVersion']['status']) {?>
            <?php echo call_user_func_array( $_smarty_tpl->smarty->registered_plugins[Smarty::PLUGIN_FUNCTION]['l'][0], array( array('s'=>'The PHP cURL extension must be enabled on your server.','mod'=>'paypal'),$_smarty_tpl ) );?>

          <?php } elseif ((($tmp = @$_smarty_tpl->tpl_vars['vars']->value['tlsVersion'])===null||$tmp==='' ? false : $tmp)) {?>
            <?php echo call_user_func_array( $_smarty_tpl->smarty->registered_plugins[Smarty::PLUGIN_FUNCTION]['l'][0], array( array('s'=>'The PHP cURL extension must be enabled on your server. Please contact your hosting provider for more information.','mod'=>'paypal'),$_smarty_tpl ) );?>

            <?php echo call_user_func_array($_smarty_tpl->registered_plugins[ 'modifier' ][ 'escape' ][ 0 ], array( $_smarty_tpl->tpl_vars['vars']->value['tlsVersion']['error_message'],'htmlall','UTF-8' ));?>

          <?php }?>
        </li>
      <?php }?>

      <?php if ((($tmp = @$_smarty_tpl->tpl_vars['vars']->value['showWebhookState'])===null||$tmp==='' ? false : $tmp)) {?>
        <?php if ($_smarty_tpl->tpl_vars['vars']->value['isWebhookEnabled']) {?>
          <li class="d-flex">
              <?php $_smarty_tpl->_subTemplateRender(($_smarty_tpl->tpl_vars['moduleFullDir']->value).("/views/templates/admin/_partials/icon-status.tpl"), $_smarty_tpl->cache_id, $_smarty_tpl->compile_id, 0, $_smarty_tpl->cache_lifetime, array('isSuccess'=>(($tmp = @$_smarty_tpl->tpl_vars['vars']->value['webhookState'])===null||$tmp==='' ? false : $tmp)), 0, true);
?>
              <?php if ((isset($_smarty_tpl->tpl_vars['vars']->value['webhookStateMsg']))) {
echo $_smarty_tpl->tpl_vars['vars']->value['webhookStateMsg'];
}?>
          </li>
        <?php } else { ?>
          <li class="d-flex">
              <?php $_smarty_tpl->_subTemplateRender(($_smarty_tpl->tpl_vars['moduleFullDir']->value).("/views/templates/admin/_partials/icon-status.tpl"), $_smarty_tpl->cache_id, $_smarty_tpl->compile_id, 0, $_smarty_tpl->cache_lifetime, array('isSuccess'=>false), 0, true);
?>
              <?php echo call_user_func_array( $_smarty_tpl->smarty->registered_plugins[Smarty::PLUGIN_FUNCTION]['l'][0], array( array('s'=>'Webhook is disabled','mod'=>'paypal'),$_smarty_tpl ) );?>

          </li>
        <?php }?>
      <?php }?>
    </ul>
  </div>

  <div class="col-12 col-lg-3 col-xl-4 align-items-end d-flex justify-content-end">
    <button class="btn btn-secondary ml-auto" refresh-technical-checklist><?php echo call_user_func_array( $_smarty_tpl->smarty->registered_plugins[Smarty::PLUGIN_FUNCTION]['l'][0], array( array('s'=>'Refresh','mod'=>'paypal'),$_smarty_tpl ) );?>
</button>
  </div>

</div>
<?php }
}
